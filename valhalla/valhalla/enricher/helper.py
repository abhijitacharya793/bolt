import json

import requests


# API OBJECT
class API:
    def __init__(self, uuid, target, root_domain, domain, protocol, protocol_version, port, method, path, body,
                 header_object, query_object):
        self.uuid = uuid
        self.target = target
        self.root_domain = root_domain
        self.domain = domain
        self.protocol = protocol
        self.protocol_version = protocol_version
        self.port = port
        self.method = method
        self.path = path
        self.body = body
        self.header_object = header_object
        self.query_object = query_object

    def __str__(self):
        api_string = f"{self.method} {self.path}?"
        # ADD QUERY PARAM
        for query_param in self.query_object:
            api_string += f"{query_param['name']}={query_param['value']}&"
        api_string += f" {self.protocol_version}\n"
        for header in self.header_object:
            api_string += f"{header['name']}: {header['value']}\n"
        return api_string


def get_api_details(uuid):
    header = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/header/?uuid={uuid}").text)
    query_param = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/query/?uuid={uuid}").text)
    api = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/?uuid={uuid}").text)[0]
    api = API(api['uuid'], api['target'], api['root_domain'], api['domain'], api['protocol'], api['protocol_version'],
              api['port'], api['method'], api['path'], api['body'], header, query_param)
    return api


def get_risk_details():
    return json.loads(requests.get(f"http://yggdrasil-api:8337/yggdrasil/v1/risk/vulnerability/").text)

def get_fuzzing_details(id):
    return json.loads(requests.get(f"http://yggdrasil-api:8337/yggdrasil/v1/risk/fuzzing/{id}").text)


def boolean_risk(api, risks):
    print("&&&& target", api.target)
    print("&&&& root domain", api.root_domain)
    print("&&&& domain", api.domain)
    print("&&&& protocol", api.protocol)
    print("&&&& protocol version", api.protocol_version)
    print("&&&& port", api.port)
    print("&&&& method", api.method)
    print("&&&& path", api.path)
    print("&&&& body", api.body)
    print("&&&& header", api.header_object)
    print("&&&& query", api.query_object)
    # TODO: Make these vulnerability checks configurable at yggdrasil
    tasks = []
    
    vulnerabilities = get_risk_details()
    for vulnerability in vulnerabilities:
        if len(vulnerability['fuzzing_rules']) > 0:
            # print(vulnerability['fuzzing_rules'])
            variables={}
            for fuzzing_rule in vulnerability['fuzzing_rules']:
                fuzzing_rule_str = get_fuzzing_details(fuzzing_rule)
                exec("condition="+fuzzing_rule_str["condition"], {'api': api}, variables)
            if variables["condition"]:
                tasks.append(str(vulnerability["id"]))
        
    return ",".join(tasks)


def enrich_api(api, risks):
    calculated_risks = boolean_risk(api, risks)
    return calculated_risks
