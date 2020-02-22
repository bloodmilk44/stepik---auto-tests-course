from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # заполняем поля
    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input3.send_keys("test@test.ru")
    # загружаем файл
    current_dir = os.path.abspath(os.path.dirname(''))
    file_path = os.path.join(current_dir, 'textfile.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    # нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
