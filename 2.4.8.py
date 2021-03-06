from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
# ждем $100
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_id('book')
    book.click()
# считаем переменную
    iks = browser.find_element_by_css_selector("#input_value").text
    print(iks)
    x = int(iks)
    y = calc(x)
# ввод ответа
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
# клик Submit
    submit = browser.find_element_by_css_selector('#solve')
    submit.click()

finally:
    browser.quit()