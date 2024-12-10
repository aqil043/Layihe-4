import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Fixture - WebDriver yaradılması və bağlanması
@pytest.fixture
def driver():
    chrome_options = Options()
    service = Service("chromedriver.exe")  # ChromeDriver yolunu müvafiq olaraq dəyişin
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver  # Testdən sonra bağlanacaq
    driver.quit()

# Test 1: Logo ölçülərinin yoxlanılması
def test_logo_width(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/a/img')
    assert element1.value_of_css_property("width") == "160px", "Logo genişliyi səhvdir"
def test_logo_height(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/a/img')
    assert element1.value_of_css_property("height") == "160px", "Logo hündürlüyü səhvdir"

# Test 2: Səhifə rənginin yoxlanılması
def test_page_color(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element2 = driver.find_element(By.XPATH, '/html/body')
    assert element2.value_of_css_property("background-color") == "rgba(0, 0, 0, 1)", "Səhifə fon rəngi düzgün deyil."

# Test 3: Cədvəl CSS xüsusiyyətinin yoxlanılması
def test_table_css(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element3 = driver.find_element(By.CLASS_NAME, "wikitable")
    assert element3.value_of_css_property("box-sizing") == "border-box", "Table box-sizing düzgün deyil."

# Test 4: Font xassələrinin yoxlanılması
def test_font_family(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        font_family = link.value_of_css_property("font-family")
        font_size = link.value_of_css_property("font-size")
        assert 'sans-serif' in font_family, f"Linkdə Sans Serif şrifti yoxdur: {link.text}"
def test_font_size(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        font_family = link.value_of_css_property("font-family")
        font_size = link.value_of_css_property("font-size")
        assert font_size == "12.6px", f"Linkin şrift ölçüsü düzgün deyil: {link.text}"
