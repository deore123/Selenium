import HtmlTestRunner
import unittest
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase (unittest.TestCase) :
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path = "../driver/geckodriver")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_serachResult(self):
        self.driver.get ("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

        WebDriverWait (self.driver , 10).until (EC.element_to_be_clickable ((By.LINK_TEXT , "No, thanks!"))).click ()

        self.driver.find_element_by_id ("sum1").send_keys ("5")
        self.driver.find_element_by_id ("sum2").send_keys ("5")

        #self.driver.find_elements_by_xpath ("//button[@onclick=\"Get Total\"]").click()
        #self.driver.find_element_by_id("gettotal").click()
        self.driver.find_element_by_css_selector ("button[onclick^='return total()']").click ()
        #https://stackoverflow.com/questions/49171370/python-selenium-how-can-click-on-onclick-elements

        #br.find_element_by_xpath ("//a[contains(@onclick,'fastener')]").click ()
        self.driver.implicitly_wait(5)


        actualVal = self.driver.find_element_by_xpath ("//*[@id=\"displayvalue\"]").text
        newVal = int(actualVal)


        print("Actual val is :== " ,newVal)

        self.assertEqual(newVal,10)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # cls.driver.quite()


if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))

   # unittest.main ()
