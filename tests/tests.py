import requests
import pytest
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def browser():
    options = Options()
    # options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_open_site():
    res = requests.get(BASE_URL)
    assert res.status_code == 200
    print(res.status_code)

def test_button_exist(browser):
    browser.get(BASE_URL+f"search?q=туалетная бумага 3 слоя&brand={BRAND_ZEWA}")
    # assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
    button_next_exist = True
    sum = 0
    count_item = WebDriverWait(browser, 70).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    # while(button_next_exist):

    browser.implicitly_wait(15)
    item = browser.find_elements(By.XPATH, XPATH_CLASS)

    p_text = item[0].text
    browser.quit()
    # print(f"Текст элемента = {p_text}, количество = {len(item)}")
        # try:
        #     next_button = browser.find_element(By.XPATH, XPATH_DOWNLOAD_NEXT)
        #     next_button.click()
        #     browser.implicitly_wait(15)
        # except NoSuchElementException:
        #     button_next_exist = False
    # print(f"Всего товаров: {sum}")
def test_canonical_link_exist(browser):
    browser.get(BASE_URL+"search?q=стеллаж")
    count_item = WebDriverWait(browser, 70).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    if count_item:
        assert len(browser.find_elements(By.XPATH, XPATH_CANONICAL_LINK)) > 0
    browser.quit()

def test_reviews_exist(browser):
    browser.get(BASE_URL + "search?q=стеллаж")
    count_item = WebDriverWait(browser, 70).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    reviews = browser.find_elements(By.CLASS_NAME, 'reviews')
    print(count_item.text)
    print(f"Count rev= {len(reviews)}")
    assert len(reviews) > 0
    browser.quit()
'css-k9eowz'
def test
    browser.quit()