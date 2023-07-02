from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    __account=(By.XPATH,"//span[contains(text(),'Account & Lists')]")
    __email=(By.NAME,"email")
    __continuebtn=(By.ID,"continue")
    __password=(By.NAME,"password")
    __signin=(By.XPATH,"//span[@id='auth-signin-button']")
    __errormsg=(By.XPATH,"//h4[contains(text(),'Incorrect phone number')]")

    def __init__(self,driver):
        self.__driver = driver

    def click_on_myacc(self):
        self.__driver.find_element(*self.__account).click()

    def set_email(self,email):
        self.__driver.find_element(*self.__email).send_keys(email)

    def click_on_continuebtn(self):
        self.__driver.find_element(*self.__continuebtn).click()

    def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_on_signin(self):
        self.__driver.find_element(*self.__signin).click()

    def verify_errormsg_is_displayed(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__errormsg))
            print('error msg is displayed')
            return True
        except:
            print('error msg is not displayed')
            return False

