import time

import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/Users/kishorekumar/Desktop/chromedriver")
    driver.get("https://backoffice.productsup.com/")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.quit()
