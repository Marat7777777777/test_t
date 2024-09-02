from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from constants import Credentials, SELECTORS


def page_load_check(browser: WebDriver, locator: str) -> bool:
    """
    Метод проверяет, что страница отображается корректно
    Если не находится элемент и возникает исключение - возвращается False
    Если нет - True
    """

    try:
        browser.find_element(By.XPATH, locator)
        WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.TAG_NAME, "html")))
    except:
        return False
    return True


def check_element(browser: WebDriver, locator: str) -> bool:
    """
    Ф-я для проверки сообщения наличия элемента на странице
    Если есть элемент - возвращаем True под assert
    """

    try:
        browser.find_element(By.XPATH, locator)
    except:
        return False
    return True


def authorize(browser,
              login=Credentials.NEW_USERNAME.value,
              password=Credentials.NEW_PASSWORD.value):
    """
    Авторизация в ресурс
    """
    username_input = browser.find_element(By.XPATH, SELECTORS['name_button'])
    password_input = browser.find_element(By.XPATH, SELECTORS['pass_button'])
    submit_button = browser.find_element(By.XPATH, SELECTORS['click_button'])
    username_input.send_keys(login)
    password_input.send_keys(password)
    submit_button.click()
