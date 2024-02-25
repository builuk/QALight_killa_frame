import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helper.pages import base
from helper.steps import tactic_shoes
from helper.data import base as data

@pytest.fixture(scope="module")
def browser():
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)
    yield driver

def open_tourism_and_camping_category(browser):
    home = base.BasePage(browser)
    home.open()
    home.open_menu().click()
    home.open_tourism_camping().click()
    assert browser.title == data.tourism_and_camping

def quantity_of_tourism_and_camping_equipments_categories(browser):
    tourism = base.TourismCamping(browser)
    home = base.BasePage(browser)
    home.open()
    home.open_menu().click()
    home.open_tourism_camping().click()
    assert tourism.check_tourist_equipment_category_list() == data.quantity_of_tourist_equipment_category_list

def check_opening_generators_and_charging_stations_link(browser):
    home = base.BasePage(browser)
    home.open()
    home.open_menu().click()
    home.open_tourism_camping().click()
    assert browser.title == data.generators_and_charging_stations_link
