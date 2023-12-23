import os
import click
import time

from src.config import PWD


@click.command()
@click.option('-t', '--template', type=click.Path(exists=True), prompt="Enter template", help="Template path")
@click.option('-w', '--working_dir', type=click.Path(exists=True), prompt="Enter working directory",
              help="Working directory")
@click.option('-o', '--output_template', prompt="Enter output path", help="Output path")
@click.option('-r', '--requests', type=click.Path(exists=True), prompt="Enter requests", help="Requests")
def cli(template, working_dir, output_template, requests):
    """
    CREATE NUCLEI TEMPLATE
    """

    # OPEN REQUEST FILES
    request_files = os.listdir(requests)
    request_list = []
    for request_file in request_files:
        with open(requests + request_file, 'r') as r_file:
            request_list.append(r_file.read())

    # TAB REQUESTS
    requests_tabbed = []
    for request in request_list:
        request_tabbed = []
        for req_line in request.split("\n"):
            request_tabbed.append("        " + req_line)
        requests_tabbed.append("\n".join(request_tabbed))

    # OPEN TEMPLATE
    try:
        os.mkdir(f"{working_dir}/{output_template}")
    except:
        pass
    for request in requests_tabbed:
        with open(template, 'r') as nuclei_template:
            content = nuclei_template.read()
            content = content.replace('{{RAW_REQUESTS}}', request)
            content = content.replace('{{PATH}}', PWD)

        with open(f"{working_dir}/{output_template}/{time.time()}.yaml", 'w') as output:
            output.write(content)
    print(f'{working_dir}/{output_template}/')


cli()
