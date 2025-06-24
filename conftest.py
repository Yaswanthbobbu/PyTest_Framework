import os
from os import mkdir
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



# Fixture to initialize browser
@pytest.fixture(scope="function")
def setup(request):
    options = Options()
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

# Hook for adding screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.cls.driver if hasattr(item.cls, 'driver') else None
        if driver:
            mkdir("Screenshot")
            screenshot_path = os.path.join("Screenshot", f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            # Attach to report

            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=item.name, attachment_type=allure.attachment_type.PNG)

            # if 'pytest_html' in item.config.pluginmanager.list_name_plugin():
            #     extra = getattr(rep, 'extra', [])
            #     extra.append(pytest_html.extras.image(screenshot_path))
            #     rep.extra = extra

# Needed for pytest-html plugin
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

# def capture_screenshot(self,screenshot_path):
#     self.driver.save_screenshot(screenshot_path)
