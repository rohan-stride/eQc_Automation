import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from pageObject.loginPage import LoginPage
from pageObject.homePage import HomePage
from utilities.baseClass import BaseClass
class Test1(BaseClass):
    def test_login(self, setup):
        loginPage = LoginPage(self.driver)
        time.sleep(3)
        actualTitle = self.driver.title

        assert actualTitle == loginPage.title
        print(actualTitle)

        loginPage.enterUserName(self.driver).clear()
        loginPage.enterUserName(self.driver).send_keys("qa")
        loginPage.enterPassword(self.driver).clear()
        loginPage.enterPassword(self.driver).send_keys("qa@eqc")
        loginPage.clickSignInBtn(self.driver).click()

    def test_docView(self, setup):
        homePage = HomePage(self.driver)
        time.sleep(3)
        homePage.clickDocView(self.driver).click()

    def test_logout(self, setup):
        homePage = HomePage(self.driver)
        time.sleep(3)
        #actualTitle = self.driver.title

        #assert actualTitle == homePage.title
        #print(actualTitle)

        homePage.toggleUserIcon(self.driver).click()
        homePage.toggleLogout(self.driver).click()
        time.sleep(3)







