from selenium import webdriver

def main():
    browser_path = "/usr/bin/brave-browser"

    option = webdriver.ChromeOptions()
    option.binary_location = browser_path

    browser = webdriver.Chrome(options=option)

    browser.get("https://www.epicgames.com/store/en-US/free-games")

if __name__ == "__main__":
    main()