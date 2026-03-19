from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_pages import BasePages
from pages.locators import main_page_locators as locators


class MainPage(BasePages):
    pages_url = '/'  # Главная страница

    def open_product_page(self):
        product_image = self.wait.until(EC.element_to_be_clickable(locators.PRODUCT_IMAGE))
        product_image.click()

    def add_to_cart_from_product(self):
        add_to_cart = self.wait.until(EC.element_to_be_clickable(locators.ADD_TO_CART_BUTTON))
        add_to_cart.click()
        continue_shopping = self.wait.until(EC.element_to_be_clickable(locators.CONTINUE_SHOPPING_BUTTON))
        continue_shopping.click()

    def hover_and_add_to_cart(self):
        product_image = self.wait.until(EC.presence_of_element_located(locators.PRODUCT_IMAGE))
        actions = ActionChains(self.driver)
        actions.move_to_element(product_image).perform()
        cart_button = self.wait.until(EC.element_to_be_clickable(locators.PRODUCT_IMAGE_HOVER_CART)        )
        cart_button.click()

    def open_cart(self):
        self.wait.until(EC.presence_of_element_located(locators.CART_QUANTITY))
        cart_link = self.wait.until(EC.element_to_be_clickable(locators.CART_LINK))
        cart_link.click()
        self.wait.until(EC.url_contains("/shop/cart"))

    def verify_product_title_in_cart(self, expected_title):
        product_title = self.wait.until(EC.presence_of_element_located(locators.PRODUCT_TITLE_IN_CART))
        assert product_title.text == expected_title

    def verify_product_code_in_cart(self, expected_code):
        product_code = self.wait.until(EC.presence_of_element_located(locators.PRODUCT_CODE_IN_CART))
        assert product_code.text == expected_code

    def verify_product_price_in_cart(self, expected_price):
        price_element = self.wait.until(EC.presence_of_element_located(locators.PRODUCT_PRICE))
        assert price_element.text == expected_price
