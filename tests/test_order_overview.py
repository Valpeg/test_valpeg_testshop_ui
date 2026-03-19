def test_valid_user_login(login_page):
    login_page.open_page()
    login_page.login('valpegushin@yandex.ru', '19711603')
    login_page.verify_login_success("My account")

def test_login_wrong_password(login_page):
    login_page.open_page()
    login_page.login('valpegushin@yandex.ru', '1111111')
    login_page.get_error_message("Wrong login/password")

def test_search_functionality(search_page):
    search_page.open_page()
    search_page.search_product("Customizable Desk")
    search_page.verify_search_results("Search Results")