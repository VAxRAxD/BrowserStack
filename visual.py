import os, json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

bstack_options = {
    "osVersion" : "14",
	"deviceName" : "iPhone 12",
    "browserName" : "Chrome",
    "buildName" : "browserstack-build-13",
    "sessionName" : "BStack single python",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY,
}

bstack_options["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
browser = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
try:
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}')
except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
browser.quit()