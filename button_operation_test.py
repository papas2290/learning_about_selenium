from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # browser.get("http://suninjuly.github.io/wait1.html")
    browser.get("http://suninjuly.github.io/cats.html")

    # button = browser.find_element_by_id("verify")
    browser.find_element_by_id("button")
    # button.click()
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text
finally:
    browser.quit()
