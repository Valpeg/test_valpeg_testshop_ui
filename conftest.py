from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
from allure_commons.types import AttachmentType
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
    options.page_load_strategy = 'none'
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver.set_page_load_timeout(300)
    chrome_driver.implicitly_wait(30)
    chrome_driver.maximize_window()
    yield chrome_driver
    allure.attach(
        chrome_driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG
    )
    chrome_driver.quit()


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
