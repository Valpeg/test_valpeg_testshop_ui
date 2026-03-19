from selenium.webdriver.common.by import By

# Login page locators
SIGN_IN_BUTTON = (By.XPATH, "(//a[contains(text(), 'Sign in')])[1]")
EMAIL_INPUT = (By.XPATH, "//input[@id='login']")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
MY_ACCOUNT_HEADER = (By.XPATH, "//h3[text()='My account']")
ERROR_MESSAGE = (By.XPATH, "//p[@role='alert']")

# Search page locators
SEARCH_ICON = (By.CSS_SELECTOR, "i.oi.oi-search.fa-stack.lh-lg")
SEARCH_INPUT = (By.XPATH, "(//input[@type='search'])[2]")
SEARCH_BUTTON = (By.XPATH, "//div[@id='o_search_modal']//button[@type='submit' and contains(@class, 'oe_search_button')]")
SEARCH_RESULTS_TITLE = (By.XPATH, "//div[text()='Search Results']")