import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture()
def browser():
    print('\nstart browser for test_fixture8...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser test_fixture8..')
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print('smoke')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('regression')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
