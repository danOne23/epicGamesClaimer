from selenium import webdriver
import os


def main():
    browser_path = os.environ["BROWSER_PATH"]

    browser = ""
    if browser_path == "":
        browser = webdriver.Chrome()
    else:
        option = webdriver.ChromeOptions()
        option.binary_location = browser_path

        browser = webdriver.Chrome(options=option)

    browser.get("https://www.epicgames.com/store/en-US/free-games")


if __name__ == "__main__":
    main()
