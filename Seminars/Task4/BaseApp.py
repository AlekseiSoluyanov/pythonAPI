from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# реализация класса работы с веб-страницей

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    # настроили явное ожидание
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Сant find element by {locator}')

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    # ДЗ№3 ФОРМА CONTACT US
    def switch_to_alert(self):
        alert_obj = self.driver.switch_to.alert
        return alert_obj.text
    