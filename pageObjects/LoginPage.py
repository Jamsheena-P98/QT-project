import time

from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

LOGIN_ICON = (By.XPATH, "//a[@class='c-account-btn']")
EMAIL = (By.XPATH, "//input[@id='username']")
PASSWORD = (By.XPATH, "//input[@id='password']")
SIGNIN_BTN = (By.XPATH, "//button[@type='submit']")


class LoginPage(BasePage):

   def click_login(self):
     super().click(LOGIN_ICON, 5)

   def qt_login_icon_display(self):
     return super().is_element_present(LOGIN_ICON, 5)

   def set_email(self, text):
     super().set_value(EMAIL, text)

   def set_pwd(self, text):
     super().set_value(PASSWORD, text)

   def click_signin(self):
     super().click(SIGNIN_BTN, 5)


