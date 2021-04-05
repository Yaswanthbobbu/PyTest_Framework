from selenium import webdriver
import pytest

class TestOrange():

    @pytest.yield_fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def testhomepage(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM"
    def testlogin(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"


# Run : pytest -v -s --html=.\assets\report.html  Test_OrangeHRM.py
# customize : pytest -v -s --html=report.html --self-Contained-html  Test_OrangeHRM.py