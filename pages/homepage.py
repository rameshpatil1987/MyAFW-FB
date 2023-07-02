from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    __cart = (By.XPATH, "//span[contains(text(),'Cart')]")

    def __init__(self, driver):
        self.__driver = driver

    def verify_home_is_displayed(self, wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__cart))
            print('homepage is displayed')
            return True
        except:
            print('homepage is not displayed')
            return False
