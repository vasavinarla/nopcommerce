import time

from selenium.webdriver.common.by import By

class editcustomer:
    lnk_customer_menu_xpath = "//ul[@role='menu']/li[4]/a/p"
    lnk_customer_xpath = "//ul[@role='menu']/li[4]/ul/li[1]/a/p"
    input_email_id = "SearchEmail"
    btn_search_id = "search-customers"
    table_row_xpath = "//table[@id='customers-grid']/tbody/tr"
    btn_edit_xpath="//table[@id='customers-grid']/tbody/tr[1]/td[7]/a"
    btn_active_xpath="//*[@id='Active']"
    btn_editsave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    alert_success_xpath="/html/body/div[3]/div[1]/div[1]"


    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMainMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def clickCustomerLink(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_xpath).click()

    def SearchbyEmail(self, email):
        self.driver.find_element(By.ID,self.input_email_id).send_keys(email)
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def EditCustomer(self, email):
        time.sleep(3)
        row_count = len(self.driver.find_elements(By.XPATH, self.table_row_xpath)) # returns webelements in list
        #print("Row Count", row_count)
        for r in range(1, row_count+1):
            print("customer name:",self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text)
            if email == self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text:
               self.driver.find_element(By.XPATH,self.btn_edit_xpath).click()
               self.driver.find_element(By.XPATH,self.btn_active_xpath).click()
               self.driver.find_element(By.XPATH,self.btn_editsave_xpath).click()
               return True


    def verifySucessAlert(self):
        return self.driver.find_element(By.XPATH, self.alert_success_xpath).text