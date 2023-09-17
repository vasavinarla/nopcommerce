import pytest
from selenium import webdriver

from Utilities.readconfig import ReadConfig

@pytest.fixture()
def setup(browser):
    base_url =ReadConfig.getApplicationURL()
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj=Service(r"D:\Selenium\chromedriver.exe")
        driver=webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"D:\Selenium\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"D:\Selenium\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(base_url)
    driver.maximize_window()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata = {
        "Tester": "Vasavi",
        "Module Name": "Login",
        "Project Name": "nopcommerce",
    }


