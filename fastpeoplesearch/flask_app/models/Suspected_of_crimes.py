import time
import requests
from PIL import Image
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Suspected():
    def __init__(self, url="https://r49.fssp.gov.ru/iss/suspect_info"):
        self.url = url
        # self.PROXY = PROXY = "194.333.443.105:9014"
        self.options = options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        # options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.get_url()

    def get_url(self):
        # options.add_argument('headless')
        self.driver.set_window_size(1000, 1000)
        self.driver.get(self.url)

    def selenium_site_options(self, info) -> str:
        time.sleep(3)
        elem = self.driver.find_element(By.CLASS_NAME, "b-form__input")
        elem.clear()
        elem.send_keys(info)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.driver.save_screenshot('sus.png')
        screenshot = Image.open('sus.png')
        im_crop = screenshot.crop((100, 50, 500, 400))
        im_crop.save('captcha_sus.png', quality=95)
        im_crop.show()
        try:
            print("КАПЧА ДЕЙСТВИТЕЛЬНА ТОЛЬКО В ТЕЧЕНИЕ 10 СЕК.")
            captcha = input("Введите капчу с картинки: ")
            elem = self.driver.find_element(By.NAME, "code")
            elem.clear()
            elem.send_keys(captcha)
            elem.send_keys(Keys.RETURN)
            time.sleep(2)
        except:
            print("Не правильная капча или устарела!")
            return 0
        try:
            print(11)
            info = self.driver.find_element(By.CLASS_NAME, "b-search-message__text").text
            if info.strip() == "По вашему запросу ничего не найдено":
                return "Не числится в базе"
            else:
                return "Числится в базе!"
        except NoSuchElementException:
            return "Неправильная капча!"
        finally:
            self.driver.close()


# n = Suspected()
# n.selenium_site_options()
