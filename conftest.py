import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    print('\nthis is conftest')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
