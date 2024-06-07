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

def test_open_site():
    res = requests.get(BASE_URL)
    assert res.status_code == 200
    print(res.text.find())

def test_img_alt_exist(browser):
    """ Проверка наличия в изображениях атрибута alt """
    browser.get(BASE_URL + f"search?q=туалетная бумага 3 слоя&brand={BRAND_ZEWA}")
    img_without_alt = browser.find_elements(By.XPATH, XPATH_IMG_WITHOUT_ALT)
    assert len(img_without_alt) == 0

def test_canonical_link_exist(browser):
    """ Проверка наличия canonical link на странице"""
    browser.get(BASE_URL + f"search?q=туалетная бумага 3 слоя&brand={BRAND_ZEWA}")
    canonical_link = browser.find_elements(By.XPATH, XPATH_CANONICAL_LINK)
    assert len(canonical_link) > 0

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

def test_button_reviews_exist(browser):
    browser.get(BASE_URL + "search?q=стеллаж")
    count_item = WebDriverWait(browser, 70).until(ec.presence_of_element_located((By.XPATH, XPATH_COUNT)))
    # reviews = browser.find_elements(By.CLASS_NAME, 'reviews')
    products = browser.find_elements(By.CLASS_NAME, 'css-k9eowz')
    button_reviews_exist = True
    for i in products:
        ActionChains(browser).move_to_element(i).pause(1).perform()
        # button_reviews_exist = button_reviews_exist and browser.find_element(By.CLASS_NAME, 'reviews').is_displayed()
        button_reviews = WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.CLASS_NAME, 'reviews')))
        if not button_reviews.is_enabled():
            button_reviews_exist = False
    # reviews_item = WebDriverWait(browser, 3).until(ec.element_to_be_clickable((By.CLASS_NAME, 'reviews')))
    assert button_reviews_exist == True
    # ActionChains(browser).click(reviews_item).perform()
    # time.sleep(5)
    # print(reviews_item.)
    # print(f"Count rev= {len(reviews)}")
    # assert len(reviews) > 0
    browser.quit()
# 'css-k9eowz'
