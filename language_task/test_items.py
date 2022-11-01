import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

"""
Если нужно будет раскомментируйте пожалуйста строчку с time.sleep(15).
А так текст кнопки выведен командой print()
pytest -sv --language=es test_items.py
pytest -sv --language=fr test_items.py
"""


def test_add_button_basket_different_language(browser):
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    )
    # time.sleep(15)
    button = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(button) > 0, '[Add to cart] button not found'
    print(f'Текст в кнопке - {button[0].text}')
