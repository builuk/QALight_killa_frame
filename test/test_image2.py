import pytest


def test_check_snikers_image2():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from helper.pages import base
    from helper.steps import tactic_shoes
    from helper.data import base as data
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)
    driver.set_window_position(2000, 600)

    tactic_shoes.open_site(driver)
    tactic_shoes.open_tactic_shoes(driver)
    assert tactic_shoes.check_image(driver) == data.sneakers_image
