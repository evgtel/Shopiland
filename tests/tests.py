import requests
import pytest
from config import BASE_URL, TEST_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser
def test_open_site():
    res = requests.get(BASE_URL)
    assert res.status_code == 200
    print(res.status_code)

def test_button_exist(browser):
    browser.get(TEST_URL)
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()