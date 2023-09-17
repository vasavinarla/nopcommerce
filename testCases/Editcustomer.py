import time

from selenium.webdriver.common.by import By

from TestData.Editcustomerdata import Customerlist
from Utilities.readconfig import ReadConfig
from Utilities.customLogger import Logger
from pageObjects.Customersearch import customerInfo
from pageObjects.loginfile import loginPage
from pageObjects.editcustomer import editcustomer


class Test004_Edit_Customer_TestSuite:
    log = Logger()

    def testCase_001_editcustomer(self, setup):
        self.log.info("*********Test Case 003 search Customer by Last name******")
        self.driver = setup
        self.log.info("*********successfully lauched application******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUsername())
        self.lp_obj.setPassword(ReadConfig.getPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clicklogin()
        self.log.info("*********Successfully Login to application******")

        self.ac_obj = editcustomer(self.driver)
        time.sleep(2)
        self.ac_obj.clickCustomerMainMenu()
        time.sleep(2)
        self.ac_obj.clickCustomerLink()

        self.ac_obj.SearchbyEmail("arthur_holmes@nopCommerce.com")
        self.status = self.ac_obj.EditCustomer("arthur_holmes@nopCommerce.com")
        if self.status==True:
            self.log.info("*********Edit Customer Successfull******")
            self.alertmsg=self.ac_obj.verifySucessAlert()
            print(self.alertmsg)
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/button').click()
            self.driver.save_screenshot("./screenshorts/testCase_001_editcustomer.png")
            print("Customer record is edited successfully")

        """for i in Customerlist:
            self.ac_obj.SearchbyEmail(i)
            self.status = self.ac_obj.EditCustomer(i)
            if self.status==True:
                self.log.info("*********Edit Customer Successfull******")
                self.alertmsg=self.ac_obj.verifySucessAlert()
                print(self.alertmsg)
                self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/button').click()
                print("Customer record is edited successfully")
                print("**********")"""



