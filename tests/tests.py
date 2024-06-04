import requests
import pytest
from config import BASE_URL, TEST_URL, XPATH_CLASS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
    browser.get(BASE_URL+"search?q=туалетная бумага 3 слоя")
    # assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
    el = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.XPATH, XPATH_CLASS)))
    col = browser.find_elements(By.XPATH, XPATH_CLASS)
    p_text = col[0].text
    print("Текст элемента = ", p_text)
    browser.quit()
