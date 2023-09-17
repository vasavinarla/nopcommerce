import random
import string

import pytest

from Utilities.readconfig import ReadConfig
from Utilities.customLogger import Logger
from pageObjects.loginfile import loginPage
from pageObjects.addCustomer import add_customers


class Test003_Add_Customer_TestSuite:
    log = Logger()

    @pytest.mark.regression

    def testCase_001_addcustomer(self, setup):
        self.log.info("*********Test Case 001 Add Customer******")
        self.driver = setup
        self.log.info("*********successfully lauched application******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUsername())
        self.lp_obj.setPassword(ReadConfig.getPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clicklogin()
        self.log.info("*********Successfully Login to application******")

        self.ac_obj = add_customers(self.driver)
        self.ac_obj.clickCustomerMainMenu()
        self.ac_obj.clickCustomerLink()
        self.ac_obj.addNewCustomer()
        self.log.info("*********Successfully launched to add customer page******")
        self.random_str=''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(8)])
        self.ac_obj.setCustomerEmail(f"{self.random_str}@gmail.com")
        self.ac_obj.setCustomerPassword("abcde")
        self.ac_obj.setCustomerFirstName("shirly")
        self.ac_obj.setCustomerLastName("mini")
        self.ac_obj.clickCustomerGender("female") # op= male or female
        self.ac_obj.setCustomerDOB("8/23/2023") # dd/mm/yyyy
        self.ac_obj.setCustomerCompany("xyz limited")
        self.ac_obj.clickTaxExemption("yes") # op=yes or no
        self.ac_obj.selectNewsLetter("Your store name") # op = "Your store name" or "Test store 2"
        self.ac_obj.selectCustomerRole("Guests") #op= "Guests" or "Registered" or "Moderators" or "Administrators" or "Vendors"
        self.ac_obj.selectVendorManager("Vendor1") # op = Vendor1 or Vendor2
        self.ac_obj.setAdminComment()
        self.log.info("*********Added customer information******")
        self.ac_obj.clickSaveButton()

        self.alertmsg = self.ac_obj.verifySucessAlert()
        print(self.alertmsg)
        if "The new customer has been added successfully" in self.alertmsg:
            self.log.info("testCase_001_addcustomer : Passed")
            self.log.info("*********Test Case 001 Add Customer completed ******")
            assert True
        else:
            self.log.error("testCase_001_addcustomer : Failed")
            self.log.info("*********Test Case 001 Add Customer completed ******")
            self.driver.save_screenshot("./screenShots/testCase_001_addcustomer.png")
            assert False










