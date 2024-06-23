from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json

options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://bstackdemo.com/')
    driver.find_element(By.ID,'offers').click()
    driver.execute_script('navigator.geolocation.getCurrentPosition = function(success){ var position = { "coords":{"latitude":"19.0760","longitude":"72.8777"}}; success(position);}')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = driver.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("fav_user\n")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = driver.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
    driver.find_element(By.ID, "login-btn").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'offers')))
    driver.find_element(By.ID, "offers").click()
    desired="We've promotional offers in your location."
    if driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div/div[1]').text==desired:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}')
    else:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Offers cannot be verified!"}}')
except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
driver.quit()