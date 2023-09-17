from selenium.webdriver.common.by import By


class loginPage:
    #kindofelem_nameofele_typelocator(variable format to store webelements)
    input_username_id="Email"
    input_password_id="Password"
    btn_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_xpath="//a[contains(text(),'Logout')]"
    link_applogo_xpath="//*[@id='ajaxBusy']"

    def __init__(self,driver):  #constructor , driver is passed here from testcase
        self.driver=driver

    def setUsername(self, email):# email value is passed from testcases
        self.driver.find_element(By.ID, self.input_username_id).clear()
        self.driver.find_element(By.ID,self.input_username_id).send_keys(email)

    def setPassword(self, password):   # password value is passed from testcases
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID,self.input_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
        Login_Page_H = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[1]/h1').text


    def applogo(self):
        status = self.driver.find_element(By.XPATH,self.link_applogo_xpath).is_displayed()
        return status






