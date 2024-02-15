#https://stackoverflow.com/questions/71002067/how-can-i-automatically-enable-notifications-in-selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from helper.pages.base import *
#123

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)

url = 'https://killa.com.ua/'
driver.get(url)


home = BasePage(driver)
shoes = TacticShoes(driver)
product = Products(driver)
time.sleep(5)
# home.open_about()
# time.sleep(5)
# home.open_delivery_and_payment()
# time.sleep(5)
# home.open_homepage()
# time.sleep(5)
home.open_tactic_shoes()
time.sleep(5)
shoes.sneakers_image()
# print(shoes.create_shoes_list())
# print(product.create_empty_image_list())
# time.sleep(5)
# home.open_guard_clothes()
# time.sleep(5)
# print(product.create_empty_image_list())
# time.sleep(5)

police = PoliceUniform(driver)

home.open_police_uniform()
time.sleep(5)
print(police.create_uniform_list())
time.sleep(3)
police.open_police_accessories()
time.sleep(3)
home.open_police_uniform()
time.sleep(3)
police.open_police_hats()
time.sleep(3)
home.open_police_uniform()
time.sleep(3)
police.open_police_shoes()
time.sleep(3)
home.open_police_uniform()
time.sleep(3)
police.open_police_clothing()
time.sleep(3)
home.open_police_uniform()
time.sleep(3)
police.open_police_equipment()
time.sleep(300)
