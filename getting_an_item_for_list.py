from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def sum_of_numbers(x, y):
    return x + y


try:
    # link = 'http://suninjuly.github.io/selects1.html'
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # browser.find_element_by_tag_name('select').click()
    # time.sleep(2)
    # browser.find_element_by_css_selector('option:nth-child(2)').click()
    # browser.find_element_by_css_selector("[value='1']").click()

    num_1 = int(browser.find_element_by_id('num1').text)
    num_2 = int(browser.find_element_by_id('num2').text)

    result = sum_of_numbers(num_1, num_2)
    # print(result)

    select = Select(browser.find_element_by_tag_name('select'))
    time.sleep(3)
    select.select_by_value(str(result))  # ищем элемент с текстом Python

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(5)
    browser.quit()
