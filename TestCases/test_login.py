
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestPages.test_page import Password_reset,LoginPage,Mainmenu_admin
class TestPassword:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Ajay"
    username1 ="Admin"
    password = "admin123"


    @pytest.fixture
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get(self.base_url)
        self.pr = Password_reset(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = Mainmenu_admin(self.driver)
        yield
        self.driver.quit()


    def test_successful_reset(self,setup_method):
        self.pr.click_password(self.username)
        self.pr.click_username(self.username)
        self.pr.click_reset(self)

    def test_successful_login(self,setup_method):
        self.lp.enter_username(self.username1)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        self.lp.pim_locator()
        self.lp.admin()

        elements_to_validate =["User Management","Job","Organization","Nationalities","Corporate Branding"
        ,"Configuration"]

        for element in elements_to_validate:
            element_displayed = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.lp.locators[element])
            ).is_displayed()
            assert element_displayed, f"{element} element is not displayed"
            print(f"{element} element is present on the page")


    def test_admin_menu(self,setup_method):
        self.ma.enter_username(self.username1)
        self.ma.enter_password(self.password)
        self.ma.click_login_button()

        elements_to_validate =["Admin","PIM","Leave","Time","Recruitment"
        ,"My Info","Performance","Dashboard","Maintenance","Buzz"]

        for element in elements_to_validate:
            element_displayed = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ma.locators[element])
            ).is_displayed()
            assert element_displayed, f"{element} element is not displayed"
            print(f"{element} element is present on the page")







