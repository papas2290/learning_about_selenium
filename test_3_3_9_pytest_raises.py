import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get('http://selenium1py.pythonanywhere.com/')
        with pytest.raises(NoSuchElementException):
            # browser.find_element_by_css_selector('button.btn')
            browser.find_element(By.CSS_SELECTOR, 'button.btn')
            pytest.fail('Не должно быть кнопки Отправить')
    finally:
        browser.quit()


def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get('http://selenium1py.pythonanywhere.com/')
        with pytest.raises(NoSuchElementException):
            # browser.find_element_by_css_selector('no_such_button.btn')
            browser.find_element(By.CSS_SELECTOR, 'no_such_button.btn')
            pytest.fail('Не должно быть кнопки Отправить')
    finally:
        browser.quit()
