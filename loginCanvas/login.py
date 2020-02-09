import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


###############
# Created : Logan Jolicoeur
# PURPOSE: Have a computer login automatically to your Canvas via Firefox or Chrome
#############

#call the driver for Firefox
driver = webdriver.Firefox()


URL = 'https://courses.uncg.edu/'
#Insert username and password directly here:
USERNAME = ''
PASSWORD = ''

def main():
    print("--CANVAS LOGIN v0.1--")
    if USERNAME == '' or PASSWORD == '':
        print("ENTER YOUR USERNAME AND PASSWORD IN THE FILE")
        driver.close()
    else:
        selection = int(input("Enter 1 for regular login or 2 for 2FA login: "))
        if(selection == 1):
            login(False)
        elif(selection == 2):
            login(True)
        else:
            print("Enter an option")
            main()

            
def login(select):
    #Retrieve the desired URL
    driver.get(URL)
    
    #Find the element and click it
    loginButton = driver.find_element_by_id("menu-item-1056").click()

    #Wait for the page to load
    driver.implicitly_wait(10)

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

    if(select):
        #2FA Authorization
        
        authorization = driver.find_element_by_id("duo_iframe")
        driver.switch_to.frame(authorization)
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[@class='positive auth-button']").click()

if __name__ == '__main__':
    main()
