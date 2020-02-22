from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять цену пока она не станет 100$
    wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    ) 
    button2 = browser.find_element_by_id("book")
    button2.click()
    # находим X
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    # вводим значение 
    value1 = browser.find_element_by_id("answer")
    value1.send_keys(y)
    # нажимаем кнопку
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
