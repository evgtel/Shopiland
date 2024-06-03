import requests
import pytest
from config import BASE_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('__headless__')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser
def test_open_site():
    res = requests.get(BASE_URL)
    assert res.status_code == 200
    print(res.status_code)

