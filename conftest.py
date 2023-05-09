import pytest

from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def driver_setup():
    if browser.driver.name in ["chrome"]:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options)
        browser.config.driver = driver

        # browser.config.driver_options = options
