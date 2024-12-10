import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)

def test_logo_size(driver, wait):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    eleLogo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.mw-wiki-logo')))
    assert eleLogo.size['width'] == 160
    assert eleLogo.size['height'] == 160

def test_featured_color(driver, wait):
    eleFeaturedDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.central-featured')))
    assert eleFeaturedDiv.value_of_css_property("background-color") == "rgba(0, 0, 0, 1)"

def test_table(driver, wait):
    eleTable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.infobox.vcard')))
    assert eleTable.value_of_css_property("box-sizing") == "border-box"

def test_font(driver, wait):
    eleFont = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'cite.citation.web.cs1')))
    assert eleFont.value_of_css_property("font-family") == "sans-serif"
    assert eleFont.value_of_css_property("font-size") == "12.6px"