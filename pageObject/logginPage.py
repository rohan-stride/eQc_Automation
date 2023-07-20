from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.maximize_window()



#---------------------------------Login


driver.get('http://staging.eqc.stride.ai')


print(driver.title)