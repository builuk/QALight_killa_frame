import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from helper.pages.base import *

option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)
driver.set_window_position(2000, 600)

def open_site(driver):
    url = 'https://killa.com.ua/'
    driver.get(url)
    #waiter
    time.sleep(5)

def open_tactic_shoes(driver):
    tactic_shoes = TacticShoes(driver)
    tactic_shoes.open_menu().click()
    #waiter
    time.sleep(5)
    tactic_shoes.open_tactic_shoes().click()

def check_image(driver):
    tactic_shoes = TacticShoes(driver)
    return tactic_shoes.sneakers_image.get_attribute('src')