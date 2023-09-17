import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.readconfig import ReadConfig
from Utilities.customLogger import Logger

from pageObjects.loginfile import loginPage


class Test001_Login_Testsuite:
    log=Logger()

    @pytest.mark.regression
    @pytest.mark.sanity

    def testcase_001_login(self, setup):
        self.log.info("****testcase_001_login****")
        self.driver = setup
        self.lp_obj = loginPage(self.driver)
        # self_lp_obj.setUsername("admin@yourstore123.com")
        # self_lp_obj.setPassword("admin")
        self.lp_obj.setUsername(ReadConfig.getUsername())
        self.lp_obj.setPassword(ReadConfig.getPassword())
        self.lp_obj.clicklogin()
        self.log.info("testcase_001_login:Login Passed")
        if self.driver.title == "Dashboard / nopCommerce administration":
            print("Title:", self.driver.title)
            print("testcase_001_login:Passed")
            time.sleep(3)
            self.lp_obj.clicklogout()
            Login_Page_H = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[1]/h1').text
            print("Login Page Header:", Login_Page_H)
            self.driver.close()
            assert True
        else:
            print("testcase_001_login:Log in Failed")
            self.log.error("Login Failed for testcase_001_login")
            self.driver.save_screenshot("./screenshorts/testcase_001_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def testcase_002_applogo(self, setup):
        self.log.info("****testcase_002_applogo****")
        self.driver = setup
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUsername())
        self.lp_obj.setPassword(ReadConfig.getPassword())
        self.lp_obj.clicklogin()
        self.log.info("testcase_002_applogo:Login Passed")
        self.status=self.lp_obj.applogo()
        if self.status==True:
            print("testcase_002_applogo:Passed")
            self.log.info("Test Case 002 Application Logo : Passed")
            self.lp_obj.clicklogout()
            self.driver.close()
            assert True
        else:
            print("testcase_002_applogo:Log in Failed")
            self.log.error("Verification Failed for testcase_002_applogo")
            self.driver.save_screenshot("./screenshorts/testcase_002_applogo.png")
            self.driver.close()
            assert False
