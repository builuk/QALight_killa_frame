#https://stackoverflow.com/questions/71002067/how-can-i-automatically-enable-notifications-in-selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from helper.pages.base import *

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
time.sleep(5)
home.open_about()
time.sleep(5)
home.open_delivery_and_payment()
time.sleep(5)
home.open_homepage()
time.sleep(300)

