import math

from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    input = browser.find_element_by_id('answer')
    # time.sleep(2)
    input.send_keys(answer)

    browser.find_element_by_id('robotCheckbox').click()
    robots_rule = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robots_rule)
    robots_rule.click()

    # time.sleep(5)

    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    # time.sleep(3)
    button.click()
finally:
    time.sleep(5)
    browser.quit()
