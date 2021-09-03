
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.userName_id = "txtUsername"
        self.userPassword_id = "txtPassword"
        self.login_button_id = "btnLogin"


    def enter_Username(self,userName):
        #self.driver.find_element_by_id("self.userName_id").clear()
        self.driver.find_element_by_id(self.userName_id).send_keys(userName)
    def enter_Password(self, userPassword):
        #self.driver.find_element_by_id("self.userPassword_id").clear()
        self.driver.find_element_by_id(self.userPassword_id).send_keys(userPassword)
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

