from selenium.webdriver.common.by import By


# Main page locators
PRODUCT_IMAGE = (By.XPATH, "//img[@alt='Customizable Desk']")
PRODUCT_IMAGE_HOVER_CART = (By.XPATH, "(//a[@class='btn btn-primary a-submit' and @title='Shopping cart'])[1]")
CART_LINK = (By.XPATH, "(//a[@href='/shop/cart'])[1]")
CART_QUANTITY = (By.XPATH, "(//sup[contains(@class,'my_cart_quantity') and normalize-space()!='0'])[1]")

# Product page locators
ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")
CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@class='btn btn-secondary']")

# Cart page locators
PRODUCT_TITLE_IN_CART = (By.XPATH, "//*[contains(text(), 'Customizable Desk (Steel, White)')]")
PRODUCT_CODE_IN_CART = (By.XPATH, "(//strong[@class='product-name product_display_name'])[1]")
PRODUCT_PRICE = (By.XPATH, "//span[@data-oe-type='monetary']//span[@class='oe_currency_value']")

PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'o_sale_product_configurator_edit')]")

