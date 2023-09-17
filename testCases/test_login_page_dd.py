import time

import pytest
from selenium.webdriver.common.by import By
from Utilities.readconfig import ReadConfig
from Utilities.customLogger import Logger
from Utilities.xlutilities import *

from pageObjects.loginfile import loginPage


class Test002_Login_Testsuite:
    log=Logger()

    @pytest.mark.regression

    def testcase_02_001_login_dd(self, setup):
        self.log.info("****testcase_02_001_login_dd****")
        self.driver = setup
        self.lp_obj = loginPage(self.driver)
        self.path = "TestData/LoginData.xlsx"
        self.sheet_name = "Sheet1"
        n_row = getRowCount(self.path, self.sheet_name)
        n_col = getColoumnCount(self.path, self.sheet_name)
        self.status = []
        for r in range(2, n_row + 1):
            self.lp_obj.setUsername(readData(self.path, self.sheet_name, r, 1))
            self.lp_obj.setPassword(readData(self.path, self.sheet_name, r, 2))
            self.ex_status = readData(self.path, self.sheet_name, r, 3)
            self.log.info("*********Login to application******")
            self.lp_obj.clicklogin()

            self.log.info("testcase_02_001_login_dd:Login Passed")
            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.ex_status == "Pass":
                        self.lp_obj.clicklogout()
                        self.status.append("Passed")
                else:
                        self.driver.save_screenshot("./screenShots/testCase_02_001_logindd.png")
                        self.status.append("Failed")
            else:
                if self.ex_status == "Fail":
                        self.status.append("Passed")
                else:
                        self.driver.save_screenshot("./screenShots/testCase_02_001_logindd.png")
                        self.status.append("Failed")

            print(self.status)

        if "Failed" in self.status:
            self.log.info("testCase_02_001_login_dd : Failed")
            self.log.info("Test Case 02_001 Login with data driven testing completed ")
            assert False
        else:
            self.log.info("testCase_-2_001_login_dd : Passed")
            self.log.info("Test Case 02_001 Login with data driven testing completed ")
            assert True


