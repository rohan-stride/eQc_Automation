from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    title = "Novo Nordisk | Login"
    invalidMsg = "invalid password"


    alertMsg = (By.CSS_SELECTOR, "MuiAlert-message")
    def getAlertMsg(self, driver):
        return self.driver.find_element(*LoginPage.alertMsg)

    userName = (By.XPATH, "//input[@placeholder = 'Username...']")
    def enterUserName(self, driver):
        return self.driver.find_element(*LoginPage.userName)

    password = (By.XPATH, "//input[@placeholder='Password...']")
    def enterPassword(self, driver):
        return self.driver.find_element(*LoginPage.password)

    passwordEye = (By.CLASS_NAME, "MuiSvgIcon-root")
    def clickPasswordEye(self, driver):
        return self.driver.find_element(*LoginPage.passwordEye)

    signInBtn = (By.XPATH, "//button[@type='submit']")
    def clickSignInBtn(self, driver):
        return self.driver.find_element(*LoginPage.signInBtn)
