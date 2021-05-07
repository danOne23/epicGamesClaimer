import os
import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def clickOn(browser, xPath, timeout=10):
    for i in range(10):
        try:
            button = browser.find_element_by_xpath(xPath)
            button.click()
            return
        except:
            sleep(1)
    print('Timed out finding:', xPath)


def main():

    browser = None

    # try:
    # browser_path = os.environ["BROWSER_PATH"]
    option = webdriver.ChromeOptions()
    # option.binary_location = browser_path
    # option.add_argument("user-data-dir=/Users/henrik/Library/Application Support/Google/Chrome/Profile 2")
    # option.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=option)
    # except KeyError:
    #     print(":((((")
    #     browser = webdriver.Chrome()

    browser.get("https://www.epicgames.com/store/en-US/free-games")

    cookies = None
    with open('cookies.json') as file:
        cookies = json.load(file)

    for cookie in cookies:
        cookie.pop('sameSite')
        browser.add_cookie(cookie)

    freeGamePath = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div[3]/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a'
    clickOn(browser, freeGamePath)

    getBtnPath = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div[3]/div/div/div[2]/div[2]/div/aside/div/div/div[5]/div/button'
    clickOn(
        browser, getBtnPath)


if __name__ == "__main__":
    main()
