from enum import Enum


class Credentials(Enum):
    USERNAME = "test"
    PASSWORD = "test"
    NEW_USERNAME = "марат карамурзов"
    NEW_PASSWORD = "1234567"


LINK = "https://numizmat-forum.ru/"

SELECTORS = {
            'login_button': '//i[@class="icon fa-power-off fa-fw"]',
            'name_button': '//input[@class="inputbox autowidth"]',
            'pass_button': '//input[@id="password"]',
            'click_button': '//input[@class="button1"]',
            'error_msg': "//div[@class='error']",
            'quit_button': '//a[@class="header-avatar dropdown-trigger dropdown-toggle"]',
            'personal_chats': '//i[@class="icon fa-inbox fa-fw"]',
            'spam_button': '//input[@name="cancel"]'
             }
