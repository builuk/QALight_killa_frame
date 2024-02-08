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
        button = self.driver.find_element(By.XPATH,
                                          '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"o-nas.html")]')
        button.click()

    def open_delivery_and_payment(self):
        button = self.driver.find_element(By.XPATH,
                                          '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"dostavka-i-oplata.html")]')
        button.click()

    def open_tactic_shoes(self):
        button = self.driver.find_element(By.XPATH,
                                          '//div[contains(@class,"mainmenublock")]//div[contains(@class,"mainmenu")]')
        button.click()
        button = self.driver.find_element(By.XPATH,
                                          '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"katalog/obuv")]')
        button.click()

    def open_guard_clothes(self):
        button = self.driver.find_element(By.XPATH,
                                          '//div[contains(@class,"mainmenublock")]//div[contains(@class,"mainmenu")]')
        button.click()
        button = self.driver.find_element(By.XPATH,
                                          '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"katalog/forma-ohranyi")]')
        button.click()

    def open_police_uniform(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[contains(@class,"mainmenublock")]//div[contains(@class,"mainmenu")]')
        button1.click()
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"katalog/dlya-politsii")]')
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
    def init(self, driver):
        super().init(driver)

    def create_uniform_list(self):
         uniform_list = []
         labels = self.driver.find_elements(By.XPATH, '//div/a[contains(@href,"katalog/")]/p')
         for label in labels:
             # a = label.text
             # shoes_list.append(a.title())
             uniform_list.append(label.text)
         return uniform_list

    def open_police_accessories(self):
        button1 = self.driver.find_element(By.XPATH,
                                           '//div[@class="col-xs-12"]/div/ul/li//a[contains(@href,"aksessuaryi-dlya-politsii")]/p[contains(@style,"height:")]')
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
