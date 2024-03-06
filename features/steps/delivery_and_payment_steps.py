from behave import given, when, then
from selenium import webdriver

from QALight_killa_frame.features.pages import base_1


@when('I navigate to Homepage')
def open_homepage(context):
    context.browser = webdriver.Chrome()
    context.base_page = base_1.BasePage(context.browser)
    context.base_page.open()



@then('I switch ua language')
def switch_to_ua(context):
    context.base_page.switch_to_ua()


@given('I am on the delivery and payment page')
def open_delivery_and_payment_page(context):
    context.delivery_page = base_1.DeliveryAndPaymentPage(context.browser)
    context.delivery_page.open_delivery_and_payment()


@then('I should see the correct title')
def verify_title(context):
    assert context.base_page.get_title() == "Доставка і оплата"
