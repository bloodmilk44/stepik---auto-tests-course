from selenium import webdriver
import time
import unittest


class testRegistration(unittest.TestCase):
  def test_scenario_registration_positive(self):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("test@test.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Не совпадает')
    browser.close()
    
  def test_scenario_registration_nagative(self):
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("test@test.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Не совпадает')
    browser.close()


if __name__ == "__main__":
  unittest.main()