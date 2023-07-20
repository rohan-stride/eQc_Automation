import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:\\Novo Automation\geckodriver.exe")
        time.sleep(2)

    driver.get('https://staging.eqc.stride.ai/')
    request.cls.driver = driver

    yield
    driver.close()
