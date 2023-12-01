import pytest
from selenium import webdriver

@pytest.fixture()
def SetUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser....")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser....")
    return driver


def pytest_addoption(parser): #this will get the value from CLI/hooks
    parser.addoption("--browser")
@pytest.fixture()
def browser(request): # this will return browser to setup method
    return request.config.getoption("--browser")

########## pytest HTML Report ###########

## IT is a hook for adding environment INFO to the HTML report

def pytest_configure(config):
    # config.addinivalue_line(
    #     "markers", "regression"
    # )
    config.metadata = {
        "Project Name: Nference",
        "Module Name: Nferex Search Engine",
        "Tester: Veera"
    }



## IT is a hook for delete/modify environment INFO to the HTML report
@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



