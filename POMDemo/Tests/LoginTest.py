import unittest
from selenium import webdriver
from POMDemo.Pages.HomePgae import HomePage
from POMDemo.Pages.LoginPage import LoginPage


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Firefox(executable_path="../driver/geckodriver")
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        login.click_login()

        homePage = HomePage(driver)

        #driver.implicitly_wait(20)
        homePage.click_Welcome()
        homePage.logout_button_linkText



        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        #
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()