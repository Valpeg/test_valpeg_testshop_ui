from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_pages import BasePages
from pages.locators import products_desks_locators as locators


class ProductsDesks(BasePages):
    pages_url = '/shop/furn-9999-office-design-software-7?category=9'

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(locators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        self.wait.until(EC.text_to_be_present_in_element(locators.CART_QUANTITY, "1"))

    def verify_cart_quantity(self, expected_quantity):
        cart_element = self.find(locators.CART_QUANTITY)
        assert cart_element.text == expected_quantity

    def open_cart(self):
        second_cart_link = self.wait.until(EC.element_to_be_clickable(locators.CART_LINK))
        second_cart_link.click()

    def verify_product_title(self, expected_title):
        product_title = self.wait.until(EC.presence_of_element_located(locators.PRODUCT_TITLE))
        assert product_title.text == expected_title

    def proceed_to_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(locators.CHECKOUT_BUTTON))
        checkout_button.click()

    def verify_address_page(self, expected_text):
        address_span = self.wait.until(EC.presence_of_element_located(locators.ADDRESS_PAGE_TEXT))
        assert address_span.text == expected_text