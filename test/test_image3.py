import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helper.pages import base
from helper.steps import tactic_shoes
from helper.data import base as data
import behave

@pytest.fixture
def browser():
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()

@pytest.fixture
def browser_firefox():
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Firefox(options=option)
    yield driver
    driver.quit()

def test_check_sneakers_image_positive(browser):
    tactic = base.TacticShoes(browser)
    tactic.open()
    tactic.open_menu().click()
    tactic.open_tactic_shoes().click()
    assert tactic.sneakers_image().get_attribute('src') == data.sneakers_image

def test_check_sneakers_image_positive_f(browser_firefox):
    tactic = base.TacticShoes(browser_firefox)
    tactic.open()
    tactic.open_menu().click()
    tactic.open_tactic_shoes().click()
    assert tactic.sneakers_image().get_attribute('src') == data.sneakers_image

def test_title_positive(browser):
    tactic = base.BasePage(browser)
    tactic.open()
    assert browser.title == data.site_title