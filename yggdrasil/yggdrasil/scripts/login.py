import os
import click


@click.command()
@click.option('--api', help='')
@click.option('--target', help='')
@click.option('--domain', help='')
@click.option('--previous_output', help='')
def login(api, target, domain):
    print("########################################## IN LOGIN ##########################################")
    click.echo(f"API: {api}")
    with open(api, "r") as req_file:
        api_string = req_file.read()
    click.echo(api_string)
    output = os.popen(f"nuclei -target {target} -o output.api").read()
    click.echo(output)


if __name__ == '__main__':
    login()
