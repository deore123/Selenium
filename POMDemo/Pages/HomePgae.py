class HomePage:
    def __init__(self,driver):
        self.driver =driver
        self.welcomeLink_id = "welcome"
        self.logout_button_linkText = "Logout"

    def click_Welcome(self):
        self.driver.find_element_by_id(self.welcomeLink_id).click()
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_linkText).click()

