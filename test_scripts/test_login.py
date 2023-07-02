import pytest

from generic.base_test import BaseTest
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from generic.utility import Excel


class TestLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_validlogin(self):
        email=Excel.get_cellvalue("../data/input.xlsx","Validlogin",2,1)
        pw=Excel.get_cellvalue("../data/input.xlsx","Validlogin",2,2)
        loginpage=LoginPage(self.driver)
        loginpage.click_on_myacc()
        loginpage.set_email(email)
        loginpage.click_on_continuebtn()
        loginpage.set_password(pw)
        loginpage.click_on_signin()
        loginpage.set_password(pw)
        homepage=HomePage(self.driver)
        result=homepage.verify_home_is_displayed(self.wait)
        assert result
        print(self.driver.title)

    @pytest.mark.run(order=2)
    def test_invalidlogin(self):
        email = Excel.get_cellvalue("../data/input.xlsx", "Invalidlogin", 2, 1)
        pw = Excel.get_cellvalue("../data/input.xlsx", "Invalidlogin", 2, 2)
        loginpage = LoginPage(self.driver)
        loginpage.click_on_myacc()
        loginpage.set_email(email)
        loginpage.click_on_continuebtn()
        result=loginpage.verify_errormsg_is_displayed(self.wait)
        assert result
        print(self.driver.title)
