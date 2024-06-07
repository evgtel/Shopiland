import requests
import pytest
from config import *
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def browser():
    options = Options()
    # options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_img_alt_exist(browser):
    """ Проверка наличия в изображениях атрибута alt """
    browser.get(BASE_URL + f"search?q=туалетная бумага 3 слоя&brand={BRAND_ZEWA}")
    img_without_alt = browser.find_elements(By.XPATH, XPATH_IMG_WITHOUT_ALT)
    assert len(img_without_alt) == 0


def test_canonical_link_exist(browser):
    """ Проверка наличия canonical link на странице"""
    browser.get(BASE_URL+"search?q=стеллаж")
    count_item = WebDriverWait(browser, 70).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    if count_item:
        assert len(browser.find_elements(By.XPATH, XPATH_CANONICAL_LINK)) > 0
    browser.quit()

def test_button_reviews_exist(browser):
    browser.get(BASE_URL + "search?q=стеллаж")
    count_item = WebDriverWait(browser, 90).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    products = browser.find_elements(By.CLASS_NAME, 'css-k9eowz')
    all_reviews_exist = True
    for product in products:
        ActionChains(browser).move_to_element(product).pause(1).perform()
        button_reviews_exist = product.find_element(By.CLASS_NAME, 'reviews').is_displayed()
        all_reviews_exist = all_reviews_exist and button_reviews_exist
    assert all_reviews_exist == True
    browser.quit()

def test_response_time(browser):
    start_time = time.time()
    browser.get(BASE_URL + "search?q=стеллаж")
    count_item = WebDriverWait(browser, 90).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    delta = time.time() - start_time
    assert delta < 20