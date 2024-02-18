import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from QALight_killa_frame.helper.data import base as data
from QALight_killa_frame.helper.pages import base


@pytest.fixture
def browser():
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()


def test_title_delivery_positive(browser):
    delivery_and_payment = base.BasePage(browser)
    delivery_and_payment.open()
    delivery_and_payment.open_delivery_and_payment()
    assert browser.title == data.delivery_title
