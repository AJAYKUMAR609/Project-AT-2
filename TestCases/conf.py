from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.common()
    return driver
