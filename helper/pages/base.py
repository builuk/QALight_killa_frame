from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        button = self.driver.find_element(By.XPATH, '//div[@id="logo"]')
        button.click()

    def open_about(self):
        button = self.driver.find_element(By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"o-nas.html")]')
        button.click()

    def open_delivery_and_payment(self):
        button = self.driver.find_element(By.XPATH,
                                          '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"dostavka-i-oplata.html")]')
        button.click()

    def open_tactic_shoes(self):

        button = self.driver.find_element(By.XPATH,'//div[contains(@class,"mainmenublock")]//div[contains(@class,"mainmenu")]')
        button.click()
        button = self.driver.find_element(By.XPATH,
                                          '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"katalog/obuv")]')
        button.click()

class TacticShoes(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_shoes_list(self):

        shoes_list = []
        labels = self.driver.find_elements(By.XPATH,'//div/a[contains(@href,"katalog/")]/p')
        for label in labels:
            # a = label.text
            # shoes_list.append(a.title())
            shoes_list.append(label.text)
        return shoes_list