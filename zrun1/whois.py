import os
import click


@click.command()
@click.option('--api', help='')
@click.option('--target', help='')
@click.option('--domain', help='')
@click.option('--previous_output', help='')
def run(api, target, domain, previous_output):
    print("########################################## IN SCRIPT ##########################################")
    click.echo(f"API: {api}")
    # with open(api, "r") as req_file:
    #     api_string = req_file.read()
    # click.echo(api_string)
    output = os.popen(f"gobuster dir -u {target} -o output.api").read()
    click.echo(output)


if __name__ == '__main__':
    run()
