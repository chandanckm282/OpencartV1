import os
import time


#from conftest import setup
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString


class Test_001_AccountReg:
    baseURL = "https://demo.opencart.com/"



    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(4)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)
        time.sleep(2)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        time.sleep(1)
        #self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        #self.regpage.setConfirmPassword("abcxyz")
       # self.regpage.setPrivacyPolicy()
       # self.regpage.clickContinue()
        time.sleep(6)
        self.confmsg = self.regpage.getconfirmationmsg()
        print(self.confmsg)
        time.sleep(1)
        self.driver.close()
    def get_screenshot_as_base64(self):
        pass
        if self.confmsg == "Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "screenshots" + "test_account_reg.png")
            self.driver.close()
            assert False




