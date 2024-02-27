import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.xpath import base


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        time.sleep(3)
        self.driver.get('https://killa.com.ua/')
        time.sleep(3)

    def about_title(self):
        title_about = self.driver.find_element(By.XPATH, base.about_title)
        return title_about.text

    def open_homepage(self):
        button = self.driver.find_element(By.XPATH, base.home)
        button.click()

    def open_about(self):
        button = self.driver.find_element(By.XPATH, base.about)
        button.click()

    def open_delivery_and_payment(self):
        button = self.driver.find_element(By.XPATH, base.delivery_and_payment)
        button.click()

    def open_tactic_shoes(self):
        # waiter
        return self.driver.find_element(By.XPATH, base.tactic_shoes)

    def open_menu(self):
        # waiter
        return self.driver.find_element(By.XPATH, base.menu)


    def open_guard_clothes(self):
        button = self.driver.find_element(By.XPATH, base.menu)
        button.click()
        button = self.driver.find_element(By.XPATH, base.guard_clothes)
        button.click()

    def open_police_uniform(self):
        button1 = self.driver.find_element(By.XPATH, base.menu)
        button1.click()
        button1 = self.driver.find_element(By.XPATH, base.police_uniform)
        button1.click()


class TacticShoes(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_shoes_list(self):
        shoes_list = []
        labels = self.driver.find_elements(By.XPATH, '//div/a[contains(@href,"katalog/")]/p')
        for label in labels:
            # a = label.text
            # shoes_list.append(a.title())
            shoes_list.append(label.text)
        return shoes_list

    # def sneakers_image(self):
    #     image = self.driver.find_element(By.XPATH, base.sneakers)
    #     return image.get_attribute('src')
    def sneakers_image(self):
        return self.driver.find_element(By.XPATH, base.sneakers)

class Products(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_empty_image_list(self):
        src = "https://killa.com.ua/image/cache/catalog/image/cache/placeholder-400x300.webp"

        product_list = []
        labels = self.driver.find_elements(By.XPATH, '//div/a[contains(@href,"katalog/")]/p')
        images = self.driver.find_elements(By.XPATH, '//div/a[contains(@href,"katalog/")]/img')
        length = len(labels) if len(labels) <= len(images) else len(images)
        for i in range(length):
            if images[i].get_attribute('src') == src:
                product_list.append(labels[i].text)
            else:
                product_list.append(images[i].get_attribute('src'))
        return product_list


class PoliceUniform(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_uniform_list(self):
        uniform_list = []
        labels = self.driver.find_elements(By.XPATH, '//div/a[contains(@href,"katalog/")]/p')
        for label in labels:
            # a = label.text
            # shoes_list.append(a.title())
            uniform_list.append(label.text)
        return uniform_list

    def open_police_accessories(self):
        button1 = self.driver.find_element(By.XPATH, base.open_police_accessories)
        button1.click()

    def open_police_hats(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[@class="col-xs-12"]/div/ul/li//a[contains(@href,"golovnyie-uboryi-politsii")]')
        button1.click()

    def open_police_shoes(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[@class="col-xs-12"]/div/ul/li//a[contains(@href,"obuv-politseyskaya")]/p[contains(@style,"height:")]')
        button1.click()

    def open_police_clothing(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[@class="col-xs-12"]/div/ul/li//a[contains(@href,"odejda-politsii")]/p[contains(@style,"height:")]')
        button1.click()

    def open_police_equipment(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[@class="col-xs-12"]/div/ul/li//a[contains(@href,"politseyskoe-snaryajenie")]/p[contains(@style,"height:")]')
        button1.click()