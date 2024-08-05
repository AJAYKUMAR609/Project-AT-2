from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Password_reset:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.password_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        self.username_locator = (By.NAME, 'username')
        self.reset_password = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def click_password(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_locator)
        ).click()

    def click_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        ).send_keys(username)

    def click_reset(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.reset_password)
        ).click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.locators = {
            "username": (By.NAME, 'username'),
            "password": (By.NAME, 'password'),
            "login_button": (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'),
            "pim": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'),
            "admin": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'),
            "User Management": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'),
            "Job": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'),
            "Organization": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span'),
            "Nationalities": (By.XPATH, "//a[normalize-space()='Nationalities']"),
            "Corporate Branding": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a'),
            "Configuration": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
        }

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators["username"])
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators["password"])
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["login_button"])
        ).click()

    def pim_locator(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["pim"])
        ).click()

    def admin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["admin"])
        ).click()


class Mainmenu_admin:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.locators = {
            "username": (By.NAME, 'username'),
            "password": (By.NAME, 'password'),
            "login_button": (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'),
            "Admin": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'),
            "PIM": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'),
            "Leave": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'),
            "Time": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span'),
            "Recruitment": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'),
            "My Info": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span'),
            "Performance": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'),
            "Dashboard": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'),
            "Maintenance":(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span'),
            "Buzz": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')

        }

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators["username"])
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators["password"])
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["login_button"])
        ).click()



