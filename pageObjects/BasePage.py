from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
      self.driver = driver

    # def wait4presence(self, element, duration=10):
    #   return WebDriverWait(self.driver, duration).until(ec.presence_of_element_located(element))
    #
    # def element_click(self, element, duration=2):
    #   # el = self.wait4clickable(element, wfc_timeout)
    #   # return WebDriverWait(self.driver, duration).until(ec.element_to_be_clickable(element))
    #   # element.click()
    #   el = WebDriverWait(self.driver, duration).until(ec.element_to_be_clickable(element))(element)
    #   el.click()
    #
    # def set_val(self, element, value):
    #   element.click()
    #   element.send_keys(Keys.CONTROL + 'a')
    #   element.send_keys(Keys.DELETE)
    #   element.send_keys(value)
    #
    # def is_element_present(self, element, duration):
    #   try:
    #     WebDriverWait(self.driver, duration).until(ec.visibility_of_element_located(element))
    #     return True
    #   except TimeoutError as e:
    #     return False
    #
    # def is_text_value(self, element):
    #   element.click()
    def find_element(self, element):
      return self.driver.find_element(element)

    def wait4presence(self, element, duration=10):
      return WebDriverWait(self.driver, duration).until(ec.presence_of_element_located(element))

    def is_element_present(self, element, duration=10):
      return WebDriverWait(self.driver, duration).until(ec.visibility_of_element_located(element))

    def set_value(self, element, value):
      el = self.wait4presence(element)
      el.click()
      el.send_keys(value)

    def click(self, element, duration=10):
      el = self.wait4presence(element, duration)
      el.click()

