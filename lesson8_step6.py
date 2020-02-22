from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим Х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    # вводим ответ
    value1 = browser.find_element_by_id("answer")
    value1.send_keys(y)
    # листаем страницу
    browser.execute_script("window.scrollBy(0, 100);")
    # прокликивем значения
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
