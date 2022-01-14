import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Anton')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Ivanov')

    email = browser.find_element_by_name('email')
    email.send_keys('ivanov@mail.ru')
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(file_path)

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(4)
    browser.quit()
