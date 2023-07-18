import time
import requests
from PIL import Image
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Selenium_searching():
    def __init__(self,  s_family, fio, d_year, mail, url="https://xn--b1aew.xn--p1ai/wanted"):
        self.payload = {
            "s_family": s_family,  # фамилия
            "fio": fio,  # имя
            "d_year": d_year,
            "email": mail,
        }

        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.session = requests.Session()
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.get_url()

    def get_url(self):
        n = self.session.get(self.url, params=self.payload)
        print(n.url)
        self.driver.set_window_size(1000, 1000)
        self.driver.get(n.url)

    def selenium_site_options(self) -> str:
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(3)
        self.driver.save_screenshot('sss.png')
        screenshot = Image.open('sss.png')
        im_crop = screenshot.crop((30, 50, 400, 400))
        im_crop.save('captcha.png', quality=95)
        im_crop.show()
        captcha = input("Введите капчу с картинки: ")
        elem = self.driver.find_element(By.NAME, "captcha")
        elem.clear()
        elem.send_keys(captcha)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            info = self.driver.find_element(By.CLASS_NAME, "bs-info")
            print(info.text)
            print("Не числится в розыске!")
            return "Не числится в розыске!"
        except NoSuchElementException:
            print("Числится в розыске!")
            return "Числится в розыске!"
        finally:
            self.driver.close()
