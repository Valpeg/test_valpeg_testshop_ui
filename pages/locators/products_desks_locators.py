from selenium.webdriver.common.by import By


ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")
CART_QUANTITY = (By.CLASS_NAME, "my_cart_quantity")
CART_LINK = (By.XPATH, "(//a[@aria-label='eCommerce cart'])[1]")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h6.d-inline.align-top.h6.fw-bold")
CHECKOUT_BUTTON = (By.XPATH, "//a[@name='website_sale_main_button']")
ADDRESS_PAGE_TEXT = (By.XPATH, "//span[text()='Fill in your address']")
