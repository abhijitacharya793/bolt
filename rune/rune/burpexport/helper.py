import json
import xml.etree.ElementTree as ET
from base64 import b64decode as b64d

import requests

from .tlds import tlds


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    burp_log = []
    for item in root.findall('./item'):
        request = b64d(item.find('request').text).decode()
        url = item.find('url').text
        host = item.find('host').text
        port = item.find('port').text
        protocol = item.find('protocol').text
        method = item.find('method').text
        path = item.find('path').text
        extension = item.find('extension').text
        response_length = item.find('responselength').text

        burp_log.append(
            {"request": request, "url": url, "host": host, "port": port, "protocol": protocol, "method": method,
             "path": path, "extension": extension, "response_length": response_length})

    return burp_log


def get_params(request):
    params = []
    line1 = request.split("\r\n")[0].split(" ")[1].split("?")
    if len(line1) > 1:
        param = line1[1].split("&")
        for param_item in param:
            params.append({"name": param_item.split("=", 1)[0], "value": param_item.split("=", 1)[1]})
    else:
        params = []
    return params


def get_protocol_version(request):
    protocol_version = request.split("\r\n")[0].split(" ")[-1]
    return protocol_version


def get_headers(request):
    headers = []
    header_string = "\r\n".join(request.split("\r\n")[1:]).split("\r\n\r\n")[0]
    if header_string:
        header = header_string.split("\r\n")
        for header_item in header:
            headers.append({"name": header_item.split(":", 1)[0], "value": header_item.split(":", 1)[1]})
    else:
        headers = []
    return headers


def get_body(request):
    body_string = request.split("\r\n\r\n")
    if len(body_string) > 1 and body_string[1] != "":
        body = body_string[1]
    else:
        body = None
    return body


def get_root_domain(host):
    api_tld = ""
    for tld in tlds:
        if tld in host:
            host = host.replace(tld, "")
            api_tld = tld
    root_domain = host.split(".")[-1] + api_tld
    return root_domain


def parse_api(api_string):
    request, url, host, port, protocol, method, path, extension, response_length = api_string.values()

    # GET QUERY PARAM
    params = get_params(request)
    # GET PROTOCOL VERSION
    protocol_version = get_protocol_version(request)
    # GET HEADER
    headers = get_headers(request)
    # GET BODY
    body = get_body(request)
    # GET DOMAIN
    domain = host
    # GET ROOT DOMAIN
    root_domain = get_root_domain(host)

    return {"protocol": protocol, "protocol_version": protocol_version, "port": port, "method": method, "path": path,
            "query_param": params, "header": headers, "body": body, "target": url, "domain": domain,
            "root_domain": root_domain}


def save_api(api, scope):
    headers = api["header"]
    query_params = api["query_param"]
    del api["header"]
    del api["query_param"]

    # ADD API
    # FIXME: split is used to separate scope
    api_id = -1
    for scope_item in scope.split(","):
        if api["domain"] == scope_item or api["root_domain"] == scope_item:
            api_id = json.loads(requests.post("http://bifrost-api:8333/bifrost/v1/api/", json=api).text)['uuid']

    # ADD QUERY
    if query_params and len(query_params) > 0:
        for query_param_item in query_params:
            query_param_item["api"] = api_id
            requests.post("http://bifrost-api:8333/bifrost/v1/api/query/", json=query_param_item)
    # ADD HEADER
    if headers and len(headers) > 0:
        for header_item in headers:
            header_item["api"] = api_id
            requests.post("http://bifrost-api:8333/bifrost/v1/api/header/", json=header_item)

    return api_id


def enrich_scan(api_id, scan_id, power, scope):
    print("ENRICHER")
    requests.post("http://valhalla-api:8335/valhalla/v1/enricher/",
                  json={"scan_id": scan_id, "uuid": api_id, "power": power, "scope": scope})
    return
