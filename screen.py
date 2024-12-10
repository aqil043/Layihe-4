from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_element_screenshot(driver, element_locator, file_name):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element_locator))
    element.screenshot(file_name)

def main():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    try:
        # Open the Wikipedia NASA page
        driver.get("https://en.wikipedia.org/wiki/NASA")
        
        # Save screenshot of Wikipedia logo
        save_element_screenshot(driver, (By.CSS_SELECTOR, 'img.mw-logo-icon'), 'wikipedia.png')

        save_element_screenshot(driver, (By.CSS_SELECTOR, 'img.mw-file-element'), '220px-NASA_logo.svg.png')
    

    finally:
        driver.quit()

if __name__ == "__main__":
    main()