import time
import calc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    text = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = browser.find_element_by_id('book')
    button.click()

    x = browser.find_element_by_id('input_value').text
    answer = calc.calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)

    button_answer = browser.find_element_by_id('solve').click()
finally:
    time.sleep(5)
    browser.quit()
