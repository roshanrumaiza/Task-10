import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#positive testcase
def test_valid_login():
    try:
        # initializing the browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Url the has to be open
        driver.get("https://www.saucedemo.com/")

        #maximize the window
        driver.maximize_window()
        #get the homepage Url
        print(driver.current_url)
        time.sleep(2)

        #locate the elements and providing valid login credentials
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()

        #get the title of webpage
        print(driver.title)
        #get the Url after login to the dashboard
        print(driver.current_url)
    finally:
        driver.quit()

#negative test case
def test_invalid_login():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        #get the current url
        print(driver.current_url)
        time.sleep(2)

        #finding element and providing invalid credentials
        driver.find_element(By.ID, 'user-name').send_keys("standard")
        driver.find_element(By.ID, 'password').send_keys("secretsauce")
        driver.find_element(By.ID, 'login-button').click()
        #get the title of the webpage
        print(driver.title)
        #get the current url and unsuccessful login
        print(driver.current_url)
    finally:
        driver.quit()
