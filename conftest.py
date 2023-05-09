import pytest

from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver_setup():
    if browser.driver.name in ["chrome"]:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser.config.driver_options = options
