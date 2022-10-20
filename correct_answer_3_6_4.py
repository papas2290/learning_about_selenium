# https://stepik.org/lesson/237240/step/4?unit=209628

import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageLocator:
    loader = "//span[text()='загрузка...']"
    input_answer = "//textarea[@placeholder='Напишите ваш ответ здесь...']"
    button_send = "//button[text()='Отправить']"
    feedback = "//p[@class='smart-hints__hint']"


class TestPage(PageLocator):

    def correct_answer(self):
        answer = math.log(int(time.time()))
        return answer

    @pytest.mark.parametrize('links', [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ])
    def test_correct_answer(self, browser, links):
        wait = WebDriverWait(browser, 60)
        # print(links,   'qwe')
        link = links
        browser.get(link)
        browser.maximize_window()
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        answer = self.correct_answer()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.input_answer)))
        browser.find_element(By.XPATH, self.input_answer).send_keys(answer)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.button_send)))
        browser.find_element(By.XPATH, self.button_send).click()
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.feedback)))
        text_result = browser.find_element(By.XPATH, self.feedback).text
        print(text_result)
        assert "Correct!" in text_result, f'Correct! not equal: {text_result}'
        time.sleep(5)
