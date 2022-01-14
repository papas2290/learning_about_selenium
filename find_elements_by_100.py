from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')

    element_first_name = browser.find_element_by_class_name('first')
    element_first_name.send_keys('Ivan')

    element_last_name = browser.find_element_by_class_name('second')
    element_last_name.send_keys('Ivanov')

    element_e_mail = browser.find_element_by_class_name('third')
    element_e_mail.send_keys('ivan@mail.ru')

    element_country = browser.find_elements_by_tag_name('input')

    for element in element_country:
        element.send_keys('lala')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
