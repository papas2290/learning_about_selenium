from selenium import webdriver
import time

try:
    # link = 'http://suninjuly.github.io/registration1.html'
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # first_name = browser.find_element_by_class_name('first')
    first_name = browser.find_element_by_class_name('first_block .first')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_class_name('first_block .second_class .second')
    last_name.send_keys('Petrov')
    email = browser.find_element_by_class_name('first_block .third_class .third')
    email.send_keys('petrov@mail.ru')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(1)
# находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name('h1')
# записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text
finally:
    time.sleep(10)
    browser.quit()
