import time

from behave import given, when, then
from helper.data import base
from features.pages import base as pages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@when('I open Homepage')
def open_homepage(context):
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    context.browser = webdriver.Chrome(options=option)
    context.base_page = pages.BasePage(context.browser)
    context.base_page.open()


@then('I click on About button')
def click_about(context):
    context.base_page.open_about()
    time.sleep(10)


@given('I see title default "{title}"')
def check_title(context, title):
    actual_title = context.base_page.return_title()
    expected_title = getattr(base, title)
    assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"

# from selenium import webdriver
#
# @given('I open Homepage')
# def open_homepage(context):
#     context.browser = webdriver.Chrome()  # Пример использования браузера Chrome
#     context.browser.get("http://yourwebsite.com")
# from behave import given, when, then
#
# @given('пользователь открыл страницу с каталогом товаров')
# def step_open_catalog(context):
#     # Код для открытия страницы с каталогом товаров
#
# @when('пользователь добавляет товар "{product}" в корзину')
# def step_add_to_cart(context, product):
#     # Код для добавления товара в корзину
#
# @then('корзина должна содержать {count:d} товара')
# def step_check_cart_count(context, count):
#     # Проверка, что корзина содержит указанное количество товаров
#
# @then('сумма товаров в корзине должна быть равна сумме "{product1}" и "{product2}"')
# def step_check_cart_sum(context, product1, product2):
#     # Проверка, что сумма товаров в корзине равна сумме указанных товаров
#
