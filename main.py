from selenium import webdriver
import os


def main():
    try:
        browser_path = os.environ["BROWSER_PATH"]
        option = webdriver.ChromeOptions()
        option.binary_location = browser_path

        browser = webdriver.Chrome(options=option)
    except:
        browser = webdriver.Chrome()

    browser.get("https://www.epicgames.com/store/en-US/free-games")


if __name__ == "__main__":
    main()
