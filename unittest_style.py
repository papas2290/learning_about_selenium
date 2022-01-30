import time
import unittest
from selenium import webdriver


class TestRegistrationOnTheWebsite1(unittest.TestCase):

    def test_one(self):
        # link = 'http://suninjuly.github.io/registration1.html'
        self.link = 'http://suninjuly.github.io/registration2.html'
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        # first_name = browser.find_element_by_class_name('first')
        self.first_name = self.browser.find_element_by_class_name('first_class .first')
        self.first_name.send_keys('Ivan')
        # last_name = browser.find_element_by_class_name('.second_class .second')
        # last_name.send_keys('Petrov')
        self.email = self.browser.find_element_by_class_name('first_block .third_class .third')
        self.email.send_keys('petrov@mail.ru')
        self.button = self.browser.find_element_by_css_selector('button.btn')
        self.button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element_by_tag_name('h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert 'Congratulations! You have successfully registered!' == welcome_text
        self.assertEqual('Congratulations! You have successfully registered!', self.welcome_text)

        time.sleep(10)
        self.browser.quit()

    def test_two(self):
        self.link = 'http://suninjuly.github.io/registration2.html'
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        self.first_name_2 = self.browser.find_element_by_class_name('first_class .first')
        self.first_name_2.send_keys('Ivan')

        self.email_2 = self.browser.find_element_by_class_name('first_block .third_class .third')
        self.email_2.send_keys('petrov@mail.ru')

        self.phone = self.browser.find_element_by_class_name('second_block .first_class .first')
        self.phone.send_keys('+79856548569')

        self.address = self.browser.find_element_by_class_name('second_block .second_class .second')
        self.address.send_keys('address')

        self.button = self.browser.find_element_by_css_selector('button.btn')
        self.button.click()
        time.sleep(1)

        self.welcome_text_elt_2 = self.browser.find_element_by_tag_name('h1')
        self.welcome_text_2 = self.welcome_text_elt_2.text
        self.assertEqual('Congratulations! You have successfully registered!', self.welcome_text_2)

        time.sleep(10)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
