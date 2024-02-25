from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

def waiter_category_button (driver, xpath):
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem.click()

def waiter_category_list (driver, xpath):
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem.click()

def waiter_dispalay_images (driver, xpath):
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem.click()

