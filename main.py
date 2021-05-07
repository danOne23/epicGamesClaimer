import os
import pickle
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
from time import sleep, thread_time


def clickOn(browser, xPath, timeout=10):
    for i in range(10):
        try:
            button = browser.find_element_by_xpath(xPath)
            button.click()
            return
        except:
            sleep(1)
    print('Timed out finding:', xPath)


def getCredentials():
    with open("credentials.txt") as f:
        username = f.readline().rstrip("\n")
        password = f.readline()
        f.close()
        return [username, password]


def login(browser, email, passwd):
    emailElement = browser.find_element_by_xpath(
        '//*[@id="email"]/div/div/div/div/div/div[2]/div/form/div[1]/div/input')
    passwordElement = browser.find_element_by_xpath(
        '//*[@id="password"]/div/div/div/div/div/div[2]/div/form/div[2]/div/input')

    # emailElement.sendKeys(email)
    # passwordElement.sendKeys(passwd)


def main():

    username, password = getCredentials()

    browser = None

    try:
        browser_path = os.environ["BROWSER_PATH"]
        option = webdriver.ChromeOptions()
        option.binary_location = browser_path
        browser = webdriver.Chrome(options=option)
    except KeyError:
        browser = webdriver.Chrome()

    browser.get("https://www.epicgames.com/store/en-US/free-games")

    # pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))

    freeGamePath = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div[3]/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a'
    clickOn(browser, freeGamePath)

    getBtnPath = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div[3]/div/div/div[2]/div[2]/div/aside/div/div/div[5]/div/button'
    clickOn(
        browser, getBtnPath)
    # clickOn(browser, '//*[@id="login-with-epic"]')

    # Auto login
    while True:
        try:
            login(browser, username, password)
            break
        except:
            sleep(1)

    # Make purchase

    # clickOn(browser, '//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[4]/div/div/label/div[1]/span/i[1]')
    # clickOn(browser, '//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[5]/div/div/button')

    sleep(200)


if __name__ == "__main__":
    main()
