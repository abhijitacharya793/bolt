import os
import json
import shutil
import time

import click


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


def get_query_params(request, part):
    line = request.split("\n")[0].split(" ")[1]
    query_param_list = []
    query_base_string = line.split("?")[1] if "?" in line else None
    if query_base_string is not None:
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


# RENAME COOKIE HEADER (THIS IS TO BE ABLE TO ADD NEW COOKIE VIA SCRIPT)
def rename_cookie(request_list):
    request_injected_list = []
    for request in request_list:
        request = request.replace("Cookie", "Oldcookie")
        request_injected_list.append(request)
    return request_injected_list


# REPLACE QUERY PARAM
def replace_query(request_list, inject_string):
    request_injected_list = []
    for request in request_list:
        for query_param in get_query_params(request, "value"):
            request_injected_list.append(request.replace("=" + query_param, "=" + inject_string))
    return request_injected_list


# REPLACE HEADER
def replace_header(request_list, inject_string):
    request_injected_list = []
    headers = []
    for request in request_list:
        for header in get_headers(request, "value"):
            if header not in headers:
                headers.append(header)
                request_injected_list.append(request.replace(": " + header, ": " + inject_string))
    return request_injected_list


# REPLACE BODY
def replace_body(request_list, inject_string):
    request_injected_list = []
    for request in request_list:
        for query, param in get_body_params(request, "value"):
            if is_json(request.split("\n")[-1]):
                request_injected_list.append(request.replace(query + ": " + param, query + ": " + inject_string))
            if is_form_urlencoded(request.split("\n")[-1]):
                request_injected_list.append(request.replace(query + "=" + param, query + "=" + inject_string))
    return request_injected_list


@click.command()
@click.option('-i', '--input1', type=click.Path(exists=True), prompt="Enter request JSON path",
              help="Request JSON path")
@click.option('-w', '--working_dir', type=click.Path(exists=True), prompt="Enter working directory",
              help="Working directory")
@click.option('-p', '--positions', prompt="Enter injection position", help="Injection position - query, header, body")
@click.option('-x', '--injection_entity', prompt="Enter injection placeholder", help="Injection placeholder")
@click.option("-a", "--append", is_flag=True, default=False, show_default=True,
              help="Append requests to existing request folder")
def cli(input1, working_dir, positions, injection_entity, append):
    """
    Replace specific positions in raw request with given payload
    """
    injected_request_list = []
    with open(input1, 'r') as burp_json:
        req_json_list = request_json_list(burp_json)
        req_json_list = rename_cookie(req_json_list)
        if injection_entity == "SKIP_INJECTION":
            injected_request_list = req_json_list
        else:
            for position in positions.split(","):
                # replace_body(request_json_list(burp_json), injection_entity)
                injected_request_list += eval(f"replace_{position}(req_json_list, injection_entity)")
    if not append:
        try:
            shutil.rmtree(working_dir + f"/requests")
        except:
            pass
    try:
        os.mkdir(working_dir + f"/requests")
    except:
        pass
    for injected_request in injected_request_list:
        with open(working_dir + f"/requests/requests{time.time()}.out", "w") as output:
            output.write(injected_request)

    print(working_dir + f"/requests/")


cli()
