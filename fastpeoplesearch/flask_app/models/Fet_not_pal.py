from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__all__ = ["FetNotPal"]


class FetNotPal:
    def __init__(self, url="https://www.reestr-zalogov.ru/search/index"):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.get_url()

    def get_url(self):
        self.driver.set_window_size(1000, 1000)
        self.driver.get(self.url)

    def selenium_site_options(self, number) -> str:
        time.sleep(2)
        elem = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div/div[2]/div/form/div[1]/div[2]/input")
        time.sleep(5)
        elem.clear()
        elem.send_keys(number)
        try:
            elem.send_keys(Keys.RETURN)

            time.sleep(10)
            res = self.driver.find_element(By.CLASS_NAME, "search-error-label").text
            res = res.strip()
            if res == "По данному запросу результатов не найдено":
                return "По данному запросу результатов не найдено"
            else:
                return "Числится в базе"
        except NoSuchElementException:
                return "Ошибка!"
        finally:
            self.driver.close()


# x = FetNotPal()
# x.selenium_site_options('2333-333-333333-333')
