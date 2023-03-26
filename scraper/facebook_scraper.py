import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selectorlib import Extractor
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import streamlit as st
import re


def remove_crap(unfiltered_comments):
    filtered_comments = []
    #for comment in unfiltered_comments:
    comment = remove_crap_from_list(unfiltered_comments)
    filtered_comments.append(comment)
    return filtered_comments


def get_comments():
    driver = get_driver()
    divs = driver.find_elements(By.TAG_NAME, 'div')
    for div in divs:
        st.write(div.text)
    time.sleep(20)


def get_driver():
    options = Options()
    options.add_extension(os.getcwd() + "\cookieblocker.crx")
    options.headless = False
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(4)
    return driver


def main_scraper(website_url):
    driver = get_driver()
    driver.get(website_url)
    time.sleep(3)
    spans = driver.find_elements(By.TAG_NAME, 'span')
    for element in spans:
        try:
            if element.text == "Visa 5 kommentarer till":
                driver.execute_script("arguments[0].click();", element)
                break
        except StaleElementReferenceException:
            pass
    div_list = []
    divs = driver.find_elements(By.TAG_NAME, 'div')
    for div in divs:
        try:
            div_list.append(div.text)
        except StaleElementReferenceException:
            pass
    unfiltered_comments = list(set(div_list))
    if os.path.exists("test.txt"):
        os.remove("test.txt")
    unfiltered_comments = ' '.join(unfiltered_comments)
    with open("test.txt", "a+") as file:
        file.write(unfiltered_comments)
    time.sleep(35)