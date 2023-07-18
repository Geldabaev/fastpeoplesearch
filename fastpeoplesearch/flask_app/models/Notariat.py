from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Selenium_searching_notariat():
    def __init__(self, url="https://notariat.ru/ru-ru/help/probate-cases/"):
        self.url = url
        # PROXY = "194.147.124.105:9014"
        self.options = options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        # options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.get_url()

    def get_url(self):
        # options.add_argument('headless')
        self.driver.set_window_size(1000, 1000)
        self.driver.get(self.url)

    def selenium_site_options(self, fio) -> str:
        elem = self.driver.find_element(By.NAME, "name")
        time.sleep(10)
        elem.clear()
        elem.send_keys(fio)
        elem.send_keys(Keys.RETURN)
        try:
            info = self.driver.find_element(By.CLASS_NAME, "probate-cases__result-header")
            res = info.get_attribute('innerHTML').find('0')
            if res == -1:  # если там нету нуля, будет -1 возвращено, если там что-то другое помимо нуля, занчит он есть там
                print("Числится в базе!")
                return "Числится в базе!"
            else:
                print("Не числится в базе!")
                return "Не числится в базе!"
        except NoSuchElementException:
            print("Ошибка")
            return "Ошибка"
        finally:
            self.driver.close()


# x = Selenium_searching_notariat()
# x.selenium_site_options()
