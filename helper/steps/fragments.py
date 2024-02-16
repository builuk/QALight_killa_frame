from behave import when, given, then


@given('I am on the Killa.ua login page')
def open_killa_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    return login_page