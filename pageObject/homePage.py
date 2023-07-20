from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    title = "Novo Nordisk | Dashboard"
    successMsg = "Successfully validated"

    userIcon = (By.XPATH, "(//button[@type='button'])[3]")

    def toggleUserIcon(self, driver):
        return self.driver.find_element(*HomePage.userIcon)

    logOut = (By.XPATH, "//li[normalize-space()='Logout']")

    def toggleLogout(self, driver):
        return self.driver.find_element(*HomePage.logOut)

    uploadIcon = (By.XPATH, "//button[normalize-space()='Upload PDF']")

    def toggleUpload(self, driver):
        return self.driver.find_element(*HomePage.uploadIcon)

    browseFilesIcon = (By.XPATH, "//span[normalize-space()='Browse Files']")

    def clickBrowseFiles(self, driver):
        return self.driver.find_element(*HomePage.browseFilesIcon)

    documentDelete = (By.XPATH, "(//span[@aria-label='Delete'])[1]")

    def clickDocDel(self, driver):
        return self.driver.find_element(*HomePage.documentDelete)

    documentView = (By.XPATH, "(//span[@aria-label='View'])[1]")

    def clickDocView(self, driver):
        return self.driver.find_element(*HomePage.documentView)

    docDownload = (By.XPATH, "(//span[@aria-label='Download'])[1]")
    def clickDocDownload(self, driver):
        return self.driver.find_element(*HomePage.docDownload)

    docThreeDots = (By.XPATH, "(//tr[1]/td[8]/div[1]/span[4]")

    def clickThreedot(self, driver):
        return self.driver.find_element(*HomePage.docThreeDots)

    restartProcess = (By.XPATH, "//li[normalize-space()='Restart process']")
    def toggleRestartProcess(self, driver):
        return self.driver.find_element(*HomePage.restartProcess)

    decryptDoc = (By.XPATH, "//li[normalize-space()='Decrypt document']")
    def toggleDecryptDoc(self, driver):
        return self.driver.find_element(*HomePage.decryptDoc)

    novoIcon = (By.XPATH, "//img[@class='side-nav-logo")
    def toggleNovoIcon(self, driver):
        return self.driver.find_element(*HomePage.novoIcon)

    searchBar = (By.XPATH, "//input[@placeholder='Search by title']")
    def toggleSearch(self, driver):
        return self.driver.find_element(*HomePage.searchBar)

    rowsPerPage = (By.XPATH, "(//div[@id=':r13:'])[1]")
    def toggleRows(self, driver):
        return self.driver.find_element(*HomePage.rowsPerPage)

    rowsPerPage5 = (By.XPATH, "//li[normalize-space()='5']")
    def toggleRows5(self, driver):
        return self.driver.find_element(*HomePage.rowsPerPage5)

    rowsPerPage10 = (By.XPATH, "//li[normalize-space()='10']")
    def toggleRows10(self, driver):
        return self.driver.find_element(*HomePage.rowsPerPage10)

    rowsPerPage25 = (By.XPATH, "//li[normalize-space()='25']")
    def toggleRows25(self, driver):
        return self.driver.find_element(*HomePage.rowsPerPage25)

    rowsPerPage100 = (By.XPATH, "//li[normalize-space()='100']")
    def toggleRows100(self, driver):
        return self.driver.find_element(*HomePage.rowsPerPage100)













