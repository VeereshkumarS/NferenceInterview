import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomerLogger import LogGen
from Utilities import XLUtils
import time
from pytest import mark

class Test_002_DDT_Login:

    baseUrl = ReadConfig.getAppliacationURL()
    path = ".\\TestData\\Nfer.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, SetUp):
        self.logger.info("********** Test 002 DDT ***********")
        self.driver = SetUp
        self.driver.get(self.baseUrl)
        self.LP = LoginPage(self.driver)
        lst = []
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("The numbe rof row present in our DataSheet:", self.rows)
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("Passed...")
                    self.lp.ClickLogout()
                    lst.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("Failed...")
                    self.lp.ClickLogout()
                    lst.append("Fail")
                    # self.driver.save_screenshot(".\\Screenshots\\" + "test_DDT_Test_Login.png")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("Failed....")
                    lst.append("Fail")
                    # self.driver.save_screenshot(".\\Screenshots\\" + "test_DDT_Test_Login.png")
                elif self.expected == "Fail":
                    self.logger.info("Passed....")
                    lst.append("Pass")
        print(lst)
        if "Fail" not in lst:
            self.logger.info("*********DDT Login Test Passed Successfully.......***********")
            self.driver.close()
            assert True
        else:
            self.logger.error("Failed......")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DDT_Test_Login.png")
            self.driver.close()
            assert False

