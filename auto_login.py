from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',{'intl.accept_languages': 'en,en_US'})

try:

    driver = webdriver.Chrome(PATH,chrome_options=options)
    driver.get("https://www.instagram.com/")

    time.sleep(5)
    username = driver.find_element_by_css_selector("input[name='username']")
    password = driver.find_element_by_css_selector("input[name='password']")

    username.clear()
    password.clear()
    username.send_keys("classieguy")
    password.send_keys("tjrwls97$")

    login = driver.find_element_by_css_selector("button[type='submit']").click()

    # skip pop up automatically
    time.sleep(10)
    notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    time.sleep(10)
    notnow2 = driver.find_element_by_xpath("//button[contains(text(),'Not Now'])").click()

except (selenium.common.exceptions.InvalidSelectorException) as e:
    print(e)