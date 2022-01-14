import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    # print(x)
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('[for=robotCheckbox]')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[for=robotsRule]')
    radiobutton.click()

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
