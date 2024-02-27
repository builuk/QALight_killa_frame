import pytest


def test_check_sneakers_image():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from helper.pages import base
    from helper.data import base as data


    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)
    driver.set_window_position(2000, 600)

    url = 'https://killa.com.ua/'
    driver.get(url)
    home = base.BasePage(driver)
    shoes = base.TacticShoes(driver)
    time.sleep(5)
    home.open_tactic_shoes()
    time.sleep(5)
    shoes.sneakers_image()
    assert shoes.sneakers_image() == data.sneakers_image
