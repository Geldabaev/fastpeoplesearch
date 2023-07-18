import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(800, 1000)
url = "https://xn--b1aew.xn--p1ai/wanted"
driver.get(url)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(3)
driver.save_screenshot('sss.png')
screenshot = Image.open('sss.png')
im_crop = screenshot.crop((0, 0, 400, 100))
im_crop.save('captcha.png', quality=95)
im_crop.show()
time.sleep(10)
driver.close()
