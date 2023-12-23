import json
import time
from functools import reduce

import click

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


def change_case(str):
    return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).lower()


service = Service(executable_path="/snap/bin/geckodriver")
driver = webdriver.Firefox(service=service)


# SELENIUM EVENTS
def sel_goto(obj):
    driver.get(obj['url'])
    pass


def sel_click(obj):
    elem = driver.find_element(By.XPATH, obj['xPath'])
    elem.click()
    pass


def sel_typing(obj):
    elem = driver.find_element(By.XPATH, obj['xPath'])
    elem.send_keys(obj['typedValue'])
    pass


def sel_keyboard(obj):
    elem = driver.find_element(By.XPATH, "//html")
    # elem.send_keys(exec(f'Keys.{change_case(obj["key"]).upper()}'))
    if obj['key'] == 'Tab':
        elem.send_keys(Keys.TAB)
    elif obj['key'] == 'ArrowDown':
        elem.send_keys(Keys.ARROW_DOWN)
    elif obj['key'] == 'Enter':
        elem.send_keys(Keys.ENTER)
    pass


def sel_userNavigate(obj):
    # print(obj)
    pass


# CLI
@click.command()
@click.option('-j', '--json_file', type=click.Path(exists=True), prompt="Enter Login export", help="Login")
def cli(json_file):
    with open(json_file, 'r') as ls:
        login_script = json.loads(ls.read())
        for obj in login_script[1:]:
            exec(f"sel_{obj['eventType']}(obj)")
        time.sleep(2)
    print(";".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()]))
    driver.close()


cli()
