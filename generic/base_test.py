import pytest
import webdriver_manager
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


class BaseTest:
    @pytest.fixture(autouse=True)
    def login_logout(self):
        pfile = Properties()
        pfile.load(open("../config.properties"))
        url = pfile['url']
        browser = pfile['browser']
        ITO = pfile['ITO']
        ETO = pfile['ETO']
        usegrid = pfile['usegrid']
        grid_url = pfile['grid_url']

        if usegrid == 'no':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print('Launched chrome browser in local system')
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                print('Launched firefox browser in local system')
        else:
            if browser == 'chrome':
                browser_options = ChromeOptions()
                print('Launched chrome browser in remote system')
            else:
                browser_options=FirefoxOptions()
                print('Launched firefox browser in remote system')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(ITO)
        self.wait=WebDriverWait(self.driver,ETO)
        yield
        self.driver.quit()

