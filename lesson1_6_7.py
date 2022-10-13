from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')

    element_first_name = browser.find_element(By.CLASS_NAME, 'first')
    element_first_name.send_keys('Ivan')

    element_last_name = browser.find_element(By.CLASS_NAME, 'second')
    element_last_name.send_keys('Ivanov')

    element_e_mail = browser.find_element(By.CLASS_NAME, 'third')
    element_e_mail.send_keys('ivan@mail.ru')

    element_country = browser.find_elements(By.TAG_NAME, 'input')

    for element in element_country:
        element.send_keys('lala')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
