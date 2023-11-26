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


def parse_api(api_string):
    print(api_string)
    request, url, host, port, protocol, method, path, extension, response_length = api_string.values()
    # GET QUERY PARAM
    param = None
    # GET HEADER
    header = None
    # GET BODY
    body = ""
    # GET DOMAIN
    domain = host
    # GET ROOT DOMAIN
    api_tld = ""
    for tld in tlds:
        if tld in host:
            host = host.replace(tld, "")
            api_tld = tld
    root_domain = host.split(".")[-1] + api_tld

    print(
        f"{protocol}, {port}, {method}, {path}, {extension}, {param}, {header}, {body}, {url}, {response_length}, {domain}, {root_domain}")

    return {"protocol": protocol, "port": port, "method": method, "path": path, "query_param": param, "header": header,
            "body": body, "target": url, "domain": domain, "root_domain": root_domain}


def save_api(api):
    # ADD QUERY
    # ADD HEADER
    # ADD API
    print(api)
    requests.get("http://bifrost-api:8333/bifrost/v1/api/")
    requests.post("http://bifrost-api:8333/bifrost/v1/api/", json=api)
    return
