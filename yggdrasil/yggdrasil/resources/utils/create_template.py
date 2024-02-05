import os, json, shutil, time, click, yaml
from random import randrange


def is_json(json_object):
    try:
        json.loads(json_object)
    except ValueError as e:
        return False
    return True


def is_form_urlencoded(form_urlencoded_object):
    if "=" in form_urlencoded_object and "{" != form_urlencoded_object[0]:
        return True
    else:
        return False


# BURP JSON TO LIST
def request_json_list(request_json):
    request_list = []
    request_json_loaded = json.load(request_json)
    for req in request_json_loaded:
        request_list.append(req['request'])
    return request_list


# RENAME COOKIE HEADER (THIS IS TO BE ABLE TO ADD NEW COOKIE VIA SCRIPT)
def rename_cookie(request_list):
    request_injected_list = []
    for request in request_list:
        request = request.replace("Cookie", "Oldcookie")
        request_injected_list.append(request)
    return request_injected_list


def get_query_params(request, part):
    line = request.split("\n")[0].split(" ")[1]
    query_param_list = []
    query_base_string = line.split("?")[1] if "?" in line else None
    if query_base_string is not None and len(query_base_string) > 3:
        query_base_string = query_base_string.split("&") if "&" in query_base_string else [query_base_string]
        for query in query_base_string:
            query_param_list.append(query.split("=")[1] if part == "value" else query.split("=")[0])
    return query_param_list


def get_headers(request, part):
    header_base_string = request.split("\n")[1:]
    header_list = []

    for header in header_base_string:
        # STOP IF HEADERS ARE DONE
        if len(header) < 4:
            break
        header_list.append(header.split(": ")[1] if part == "value" else header.split(": ")[0])

    return header_list


# TODO: GET BODY PARAMS
def get_body_params(request, part):
    body_param_list = []
    body_value_list = []
    request_body = request.split("\n")[-1]
    if is_json(request_body):
        for body in request_body[1:-1].split(","):
            body_param_list.append(body.split(":")[0])
            body_value_list.append(body.split(":")[1])
    if is_form_urlencoded(request_body):
        for body in request_body.split("&"):
            body_param_list.append(body.split("=")[0])
            body_value_list.append(body.split("=")[1])
    return zip(body_param_list, body_value_list)


# %%%%%%%%%%%%%%%%%%%% REPLACE %%%%%%%%%%%%%%%%%%%%
# REPLACE QUERY PARAM
def replace_query(request, inject_string):
    requests = []
    for query_param in get_query_params(request, "value"):
        requests.append(request.replace("=" + query_param, "=" + inject_string))
    return requests


# REPLACE HEADER
def replace_header(request, inject_string):
    headers = []
    requests = []
    for header in get_headers(request, "value"):
        if header not in headers:
            headers.append(header)
            requests.append(request.replace(": " + header, ": " + inject_string))
    return requests


# REPLACE BODY
def replace_body(request, inject_string):
    requests = []
    for query, param in get_body_params(request, "value"):
        if is_json(request.split("\n")[-1]):
            requests.append(request.replace(query + ": " + param, query + ": " + inject_string))
        if is_form_urlencoded(request.split("\n")[-1]):
            requests.append(request.replace(query + "=" + param, query + "=" + inject_string))
    return requests


# %%%%%%%%%%%%%%%%%%%% REPLACE %%%%%%%%%%%%%%%%%%%%


# CREATE TEMPLATE WITH REQUEST
def write_template(template_entry, request_content):
    with open(template_entry, "r") as template_file:
        template_content = template_file.read()

    with open(f"/ragnarok/input/template{randrange(20000)}.yaml", "w") as template_file:
        template_file.write(template_content.replace("{{REQUEST}}", request_content.replace("\n", "\n        ")))


@click.command()
@click.option('--template')
def template(template):
    requests = []
    with open("request.api", "r") as request_file:
        request_content = request_file.read()
    for position in ['query', 'header', 'body']:
        requests += eval(f"replace_{position}(request_content, \"{{{{payloadStr}}}}\")")
    for request in requests:
        write_template(template, request)


if __name__ == '__main__':
    template()
