from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element_by_id('treasure')
    # print(box)
    x = box.get_attribute('valuex')
    # print(x)
    answer = calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)

    checkbox_robot = browser.find_element_by_id('robotCheckbox')
    checkbox_robot.click()

    radio_button_robot = browser.find_element_by_id('robotsRule')
    radio_button_robot.click()

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()