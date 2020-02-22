from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # кликаем по весёлой кнопке :)
    element1 = browser.find_element_by_css_selector("body > form > div > div > button")
    time.sleep(1)
    element1.click()
    # переключаемся на открытое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # находим Х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    # вводим значение 
    value1 = browser.find_element_by_id("answer")
    value1.send_keys(y)
    # нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
