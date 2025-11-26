import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#initializing the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Url the has to be open
driver.get("https://www.saucedemo.com/")

#maximizing the window
driver.maximize_window()
time.sleep(2)

#locating element, finding the field username in the page and input the value standard_user
driver.find_element(By.ID,'user-name').send_keys("standard_user")

#locating element, finding the field password in the page and input the value secret_sauce
driver.find_element(By.ID,'password').send_keys("secret_sauce")

#finding the field login-button in the page and clicking on it
driver.find_element(By.ID,'login-button').click()

#get the title of the webpage
print(f"Title of the webpage:{driver.title}")

#get the current Url of the webpage
print(f"Current Url:{driver.current_url}")

#extarct the entire webpage content.
webpage_content=driver.find_element(By.XPATH,'//body').text

#save the extracted webpage content to Webpage_task_10 text file
my_file_name=open(file='Webpage_task_10.txt', mode='w', encoding="utf-8")
my_file_name.write(webpage_content)
print("Content of the webpage saved in the file:Webpage_task_10.txt")
driver.quit()


