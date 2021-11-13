from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@type='email']")
    clickNext = (By.XPATH, "(//*[@class='btn btn-primary btn-block'])[1]")
    passwordText = (By.XPATH, "//input[@type='password']")
    clickLogin = (By.XPATH, "(//*[@class='btn btn-primary btn-block'])[2]")

    def emailText(self):
        return self.driver.find_element(*HomePage.email)

    def next(self):
        return self.driver.find_element(*HomePage.clickNext)

    def password(self):
        return self.driver.find_element(*HomePage.passwordText)

    def loginpage(self):
        return self.driver.find_element(*HomePage.clickLogin)


