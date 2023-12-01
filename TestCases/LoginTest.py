import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomerLogger import LogGen

class Test_001_Login:

    baseUrl = ReadConfig.getAppliacationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepage_title(self, SetUp):
        self.logger.info("***************** Homepage Title *******************")
        self.logger.info("***************** Verifying Homepage Title ****************")
        self.driver = SetUp
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.quit()
            self.logger.info("************* Passed ************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("************* Failed ***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, SetUp):
        self.driver = SetUp
        self.driver.get(self.baseUrl)
        self.LP = LoginPage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.ClickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_test_login.png")
            self.driver.close()
            assert False
