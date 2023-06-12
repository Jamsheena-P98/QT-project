from behave import *
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import configparser

from pageObjects.datadriven import readData

config = configparser.ConfigParser(inline_comment_prefixes=('#',))
config.read('config.ini')
global login_page


@given(u'I am logged into QT')
def step_impl(context):
    context.driver = webdriver.Chrome("./chromedriver.exe")
    context.driver.get('https://qt.io/')
    context.driver.maximize_window()


@then(u'System should display the QT site')
def step_impl(context):
    global login_page
    login_page = LoginPage(context.driver)
    if login_page.qt_login_icon_display():
        print("QT site is displayed")
    else:
        print("QT site is not displayed")


@when(u'I click on the login icon')
def step_impl(context):
    global login_page
    login_page = LoginPage(context.driver)
    login_page.click_login()


@when(u'I enter email')
def step_impl(context):
    global login_page
    xl_file = config['Folders']['QT_EXCEL_DIR'] + config['Excel']['QT_TST_LGN_XLS']
    email = readData(xl_file, "Details", 2, 1)
    login_page = LoginPage(context.driver)
    login_page.set_email(email)


@when(u'I enter password')
def step_impl(context):
    global login_page
    xl_file = config['Folders']['QT_EXCEL_DIR'] + config['Excel']['QT_TST_LGN_XLS']
    pwd = readData(xl_file, "Details", 3, 1)
    login_page = LoginPage(context.driver)
    login_page.set_pwd(pwd)


@when(u'I click on signin')
def step_impl(context):
    global login_page
    login_page = LoginPage(context.driver)
    login_page.click_signin()



