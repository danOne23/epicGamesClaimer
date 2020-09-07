from selenium import webdriver

import os
from time import sleep


def clickOn(browser, xPath):
    while True:
        try:
            button = browser.find_element_by_xpath(xPath)
            button.click()
            break
        except:
            sleep(1)


def main():
    browser = ""
    try:
        browser_path = os.environ["BROWSER_PATH"]
        option = webdriver.ChromeOptions()
        option.binary_location = browser_path

        browser = webdriver.Chrome(options=option)
    except:
        browser = webdriver.Chrome()

    browser.get("https://www.epicgames.com/store/en-US/free-games")

    freeGamePath = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div/div/div[2]/div[2]/div/div/section/div/div[1]/div/div/a'
    clickOn(browser, freeGamePath)
    clickOn(
        browser, '//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/button')
    clickOn(browser, '//*[@id="login-with-epic"]')

    # Auto login

    # Make purchase

    # clickOn(browser, '//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[4]/div/div/label/div[1]/span/i[1]')
    # clickOn(browser, '//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[5]/div/div/button')

    sleep(200)


if __name__ == "__main__":
    main()
