import sys
import os
from selenium import webdriver


def createpj(pjName):
    path = "/PATH/TO/YOUR_PROJECT/"
    os.makedirs(path+pjName)
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    loginField = driver.find_element_by_id("login_field")
    passField = driver.find_element_by_id("password")
    submitButton = driver.find_element_by_xpath(
        '//*[@id="login"]/form/div[3]/input[4]')
    loginField.send_keys('YOUR_USERNAME')
    passField.send_keys('YOUR_PASSWORD')
    submitButton.submit()
    driver.get('https://github.com/new')
    repoField = driver.find_element_by_id("repository_name")
    repoField.send_keys(pjName)
    submitButton = driver.find_element_by_xpath(
        '//*[@id="new_repository"]/div[3]/button')
    submitButton.submit()
    driver.close()


if __name__ == "__main__":
    firstArg = str(sys.argv[1])
    createpj(firstArg)
