from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button_go = browser.find_element_by_class_name('btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text

    answer = calc(x)
    input_answer = browser.find_element_by_id('answer').send_keys(answer)

    button_answer = browser.find_element_by_class_name('btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()
