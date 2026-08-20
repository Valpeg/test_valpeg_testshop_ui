from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.order_overview import OrderOverview
from pages.products_desks import ProductsDesks
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
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
