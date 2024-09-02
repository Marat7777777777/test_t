import allure
from constants import Credentials, LINK, SELECTORS
from selenium.webdriver.common.by import By
from helpers import page_load_check, check_element, authorize


@allure.title("Тест загрузки стартовой страницы")
def test_home_page(browser):
    """
    В тесте открывается стартовая страница ресурса
    Проверяется, что страница прогружается корректно
    """

    with allure.step("Открываем стартовую страницу"):
        browser.get(LINK)
    assert page_load_check(browser, SELECTORS['login_button']), 'page not load'


@allure.title("Тест логина на ресурс")
def test_login_page(browser):
    """
    Тест вводит корректные и некорректные данные для авторизации входа в личный кабинет
    Проверяется, что страница прогружается корректно
    """

    with allure.step("Открытие стартовой страницы ресурса"):
        browser.get(LINK)
    login_link = browser.find_element(By.XPATH, SELECTORS['login_button'])
    login_link.click()

    with allure.step("Ввод некорректных данных от ресурса"):
        authorize(browser, Credentials.USERNAME.value, Credentials.PASSWORD.value)
        assert check_element(browser, SELECTORS['error_msg']), "Error msg not present"

    with allure.step("Ввод корректных данных от ресурса"):
        authorize(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert check_element(browser, SELECTORS['personal_chats']), "personal chats is not visible"
    login_link = browser.find_element(By.XPATH, SELECTORS['spam_button'])
    login_link.click()
    logout_link = browser.find_element(By.XPATH, SELECTORS['quit_button'])
    logout_link.click()
    logout_link = browser.find_element(By.XPATH, SELECTORS['login_button'])
    logout_link.click()

@allure.title("Тест выхода из аккаунта")
def test_logout(browser):
    """
    Тест выходит из личного кабинета
    Проверяется, что страница прогружается корректно
    """

    with allure.step("Открытие стартовой страницы ресурса"):
        browser.get(LINK)

    login_link = browser.find_element(By.XPATH, SELECTORS['login_button'])
    login_link.click()

    with allure.step("Ввод корректных данных от ресурса"):
        authorize(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert check_element(browser, SELECTORS['personal_chats']), "personal chats is not visible"

    with allure.step("Нажатие на кнопку выхода"):
        logout_link = browser.find_element(By.XPATH, SELECTORS['quit_button'])
        logout_link.click()
        logout_link = browser.find_element(By.XPATH, SELECTORS['login_button'])
        logout_link.click()
        assert check_element(browser, SELECTORS['login_button']), "login_button is not present"
