import typer, json

from main.yggdrasil.run import Run

app = typer.Typer()


@app.command()
def install():
    print(f"Installed yggdrasil")


@app.command()
def tool(formal: bool = False):
    pass


@app.command()
def plugin(formal: bool = False):
    pass


@app.command()
def run(scan: str, api_str: str, power: int = 1):
    api = json.loads(api_str)
    print(f"Running {scan} scan with power {power} and api {api['target']}")
    task = Run(scan, power, api)
    task.execute()
