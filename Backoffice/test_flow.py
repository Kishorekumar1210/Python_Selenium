import time

import pytest
from selenium import webdriver

from TestData.LoginPageData import LoginPageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_case(self, getData):

        home = HomePage(self.driver)
        home.emailText().send_keys(getData["Email"])
        time.sleep(1)
        home.next().click()
        home.password().send_keys(getData["Password"])
        home.loginpage().click()
        time.sleep(2)
        print(self.driver.current_url)

    @pytest.fixture(params=LoginPageData.test_loginData)
    def getData(self, request):
        return request.param
