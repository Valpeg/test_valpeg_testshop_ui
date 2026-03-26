def test_add_to_cart(products_page):
    products_page.open_page()
    products_page.add_to_cart()
    products_page.verify_cart_quantity("1")


def test_add_to_cart_and_open_cart(products_page):
    products_page.open_page()
    products_page.add_to_cart()
    products_page.open_cart()
    products_page.verify_product_title("Office Design Software")


def test_add_to_cart_and_checkout(products_page):
    products_page.open_page()
    products_page.add_to_cart()
    products_page.open_cart()
    products_page.verify_product_title("Office Design Software")
    products_page.proceed_to_checkout()
    products_page.verify_address_page("Fill in your address")