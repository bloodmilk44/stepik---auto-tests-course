import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1",
                                  "236903/step/1", "236904/step/1", "236905/step/1"])
def test_parametrize(browser, link):
    link = f"https://stepik.org/lesson/{link}"
    browser.get(link)
    time.sleep(8)
    input1 = browser.find_element_by_tag_name("textarea")
    y = math.log(int(time.time()))
    answer33 = str(y)
    input1.send_keys(answer33)
    time.sleep(3)
    input2 = browser.find_element_by_css_selector(".submit-submission")
    input2.click()
    time.sleep(3)
    answer_elt = browser.find_element_by_class_name("smart-hints__hint")
    answer_text = answer_elt.text
    assert "Correct!" == answer_text
      
