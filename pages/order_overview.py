from selenium.webdriver.support import expected_conditions as EC
from pages.base_pages import BasePages
from pages.locators import order_overview_locators as locators


class OrderOverview(BasePages):
    pages_url = '/shop/cart'

    def login(self, email, password):
        sign_in_button = self.wait.until(
            EC.element_to_be_clickable(locators.SIGN_IN_BUTTON)
        )
        sign_in_button.click()
        email_input = self.find(locators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.find(locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button = self.wait.until(
            EC.element_to_be_clickable(locators.LOGIN_BUTTON)
        )
        login_button.click()

    def verify_login_success(self, text):
        my_account = self.wait.until(EC.presence_of_element_located(locators.MY_ACCOUNT_HEADER)
        )
        assert my_account.text == text

    def get_error_message(self, text):
        error_message = self.wait.until(EC.presence_of_element_located(locators.ERROR_MESSAGE)
        )
        assert error_message.text == text

    def search_product(self, product_name):
        search_icon = self.wait.until(
            EC.element_to_be_clickable(locators.SEARCH_ICON)
        )
        search_icon.click()
        search_input = self.wait.until(
            EC.element_to_be_clickable(locators.SEARCH_INPUT)
        )
        search_input.send_keys(product_name)
        search_button = self.wait.until(
            EC.element_to_be_clickable(locators.SEARCH_BUTTON)
        )
        search_button.click()

    def verify_search_results(self, expected_title):
        search_title = self.wait.until(
            EC.presence_of_element_located(locators.SEARCH_RESULTS_TITLE)
        )
        assert search_title.text == expected_title



