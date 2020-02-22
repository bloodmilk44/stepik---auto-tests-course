from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # кликаем по кнопке магического путешествия :)
    element1 = browser.find_element_by_css_selector("body > form > div > div > button")
    element1.click()
    # кликаем по всплывающему окну
    confirm = browser.switch_to.alert
    confirm.accept()
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
