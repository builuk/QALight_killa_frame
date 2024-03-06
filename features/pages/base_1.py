import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from QALight_killa_frame.helper.xpath import base, headers
from QALight_killa_frame.helper.waiters import header_waiters
from QALight_killa_frame.features.pages.base import BasePage


class DeliveryAndPaymentPage(BasePage):
    def __init__(self, driver):
            self.driver = driver

    def open_delivery_and_payment(self):
        header_waiters.wait_for_element_located(self.driver, base.delivery_and_payment)
        self.driver.find_element(By.XPATH, base.delivery_and_payment).click()


    def get_title(self):
        return self.driver.title

    def return_title(context, title):
       expected_title = getattr(base, title)
       actual_title = context.base_page.return_title(expected_title)
       assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
