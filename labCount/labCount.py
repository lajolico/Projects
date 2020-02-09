import os
import time
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Author: Logan Jolicoeur
# Purpose: Auto Log labcount forms, which are done every half hour per shift

 
##options = webdriver.FirefoxOptions()
##options.add_argument('-headless')
## 
##browser = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)
## 
##browser.get('https://www.duckduckgo.com')
## 
##browser.save_screenshot('C:\\Users\\grayson\\Downloads\\headless_firefox_test.png')
## 
##browser.quit()

driver = webdriver.Firefox()

URL = "https://its.uncg.edu/Labs/Lab_Count/"
#Insert username and password directly here:
USERNAME = 'lajolico'
PASSWORD = 'MbIs062620002001'

def login():
    driver.get(URL)
    time.sleep(2) 
    #Find the login_form and enter in username and password
    username = driver.find_element_by_id("j_username")
    username.clear()
    username.send_keys(USERNAME)
    password = driver.find_element_by_id("j_password")
    password.clear()
    password.send_keys(PASSWORD)

    submitLogin = driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

    #Wait for page to load
    time.sleep(2)

    #2FA Authorization
    
    authorization = driver.find_element_by_id("duo_iframe")
    driver.switch_to.frame(authorization)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//button[@class='positive auth-button']").click()

    labCount()



def labCount():
    
    

if __name__ == '__main__':
    login()
    
