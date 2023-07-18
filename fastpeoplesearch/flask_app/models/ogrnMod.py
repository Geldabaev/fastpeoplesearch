from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import openpyxl


def ogrn_func():
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    time.sleep(5)  # долго грузится - делаем задержку
    browser.get('https://egrul.nalog.ru/')

    for x in range(2, 187):  # 2 - A2 ячейка, 187 - A186 ячейка.
        wb = openpyxl.load_workbook('Client_side/ogrn.xlsx')
        # sheet=wb.get_active_sheet()
        sheet = wb.get_sheet_by_name('Sheet1')
        print(sheet)
        a = tuple(str(sheet.cell(row=x, column=1).value).strip())  # получаем кортеж из ОГРН в ячейке A2
        act = browser.find_element(By.ID, 'query')
        act.click()
        time.sleep(1)
        # вводим посимвольно в строку ОГРН, т.к. ввод сразу всего ОГРН не корректно обрабатывается
        i = 0
        try:
            assert a != ('N', 'o', 'n', 'e'), "Огрн проверены!"
        except AssertionError:
            break
        for i in range(13):
            act.send_keys(a[i])
            time.sleep(0.1)
            i += 1
        try:
            act = browser.find_element(By.CSS_SELECTOR, '.btn-search')
            time.sleep(0.5)
            act.click()
            time.sleep(4)
            act = browser.find_element(By.CSS_SELECTOR, 'button.btn-with-icon:nth-child(2)')
            time.sleep(0.5)
            act.click()
            time.sleep(4)
            act = browser.find_element(By.ID, 'query')
            act.click()
            # удаляем старый ОГРН
            i = 0
            for i in range(13):
                act.send_keys(Keys.BACK_SPACE)
                i += 1
        except:
            print("Огрн не найден!")
            return "Огрн не найден!"
    browser.quit()
    return "ВЫПИСКА ПО ОГРН ПОЛУЧЕН!"