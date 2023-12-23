import json
import click
import xml.etree.ElementTree as ET
from base64 import b64decode as b64d


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    burp_log = {}
    for item in root.findall('./item'):
        request = b64d(item.find('request').text).decode()
        burp_log[request.split("\n")[0].split(" HTTP/")[0].split("=")[0]] = {'request': request}

    return list(burp_log.values())


@click.command()
@click.option('-i', '--input', type=click.Path(exists=True), prompt="Enter Burpsuite export path",
              help="Burpsuite logs export path")
@click.option('-o', '--output', prompt="Enter output JSON path", help="Output JSON path")
def cli(input, output):
    with open(output, 'w') as burp_json:
        burp_json.write(json.dumps(parse_xml(input)))


cli()
