import pytest
import shutil
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    driver_path = shutil.which("geckodriver")
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()