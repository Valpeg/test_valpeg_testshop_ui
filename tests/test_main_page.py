def test_new_tab_one(main_page):
    main_page.open_page()
    main_page.open_product_page()
    main_page.add_to_cart_from_product()
    main_page.open_cart()
    main_page.verify_product_title_in_cart("Customizable Desk (Steel, White)")

def test_cart_button(main_page):
    main_page.open_page()
    main_page.hover_and_add_to_cart()
    main_page.click_proceed_to_checkout()
    main_page.verify_product_title_in_cart("Customizable Desk (Steel, White)")

def test_new_tab_two(main_page):
    main_page.open_page()
    main_page.open_product_page()
    main_page.add_to_cart_from_product()
    main_page.open_cart()
    main_page.verify_product_price_in_cart("750.00")
