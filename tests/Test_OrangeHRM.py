from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.usefixtures("setup")
class TestOrange:
    driver: WebDriver

    def test_homepage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(6)
        assert self.driver.title=="OrangeHRM"
    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(6)
        self.driver.find_element(By.CSS_SELECTOR,"input[name=username1]").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[name=password]").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
        time.sleep(6)
        assert self.driver.title=="OrangeHRM"


# Run : pytest -v -s tests/Test_OrangeHRM.py --html=Report\report.html
# Allure : pytest tests/Test_OrangeHRM.py --alluredir=allure-results
# allure generate allure-results --clean -o allure-report