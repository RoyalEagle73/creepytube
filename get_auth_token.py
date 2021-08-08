from time import sleep
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthTokenizer():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.config = ConfigParser(interpolation=None)
        self.config.read('config.cfg')
        self.email = self.config['GMAIL']['email']
        self.password = self.config['GMAIL']['password']

    def get_auth_token(self, url):
        self.driver.get(url)
        email_phone = self.driver.find_element_by_xpath("//input[@id='identifierId']")
        email_phone.send_keys(self.email)
        self.driver.find_element_by_id("identifierNext").click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(self.password)
        self.driver.find_element_by_id("passwordNext").click()

        sleep(5)
        
        self.driver.find_element_by_link_text('Advanced').click()
        self.driver.find_element_by_link_text('Go to Creep Tube (unsafe)').click()
        
        sleep(5)
        
        self.driver.find_element_by_id('i3').click()
        self.driver.find_elements_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc xYnMae TrZEUc lw1w4b']")[1].click()
        
        sleep(5)

        token = self.driver.find_element_by_xpath("//textarea[@class='fD1Pid']").get_attribute('innerHTML')
        self.driver.close()
        return token