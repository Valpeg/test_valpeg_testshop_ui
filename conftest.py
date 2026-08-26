from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.order_overview import OrderOverview
from pages.products_desks import ProductsDesks
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--remote-debugging-port=9222')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_page_load_timeout(30)
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


@pytest.fixture()
def login_page(driver):
    return OrderOverview(driver)


@pytest.fixture()
def search_page(driver):
    return OrderOverview(driver)


@pytest.fixture()
def products_page(driver):
    return ProductsDesks(driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)
