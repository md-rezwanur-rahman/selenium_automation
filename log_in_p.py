from selenium import webdriver
from selenium.webdriver.common.by import By as B

class log_inp:
    def __init__(self):
        self.d=webdriver.Edge()
    def webload(self):
        self.d.get("https://www.saucedemo.com/")
        self.d.maximize_window()
    def log_in(self,user_name,password):
        user = self.d.find_element(B.XPATH,"//input[@id='user-name']")
        pasw = self.d.find_element(B.XPATH,"//input[@id='password']")
        lbtn = self.d.find_element(B.XPATH,"//input[@id='login-button']")
        input('Enter To send User Name:')
        user.send_keys(user_name)
        input('Enter To send Password:')
        pasw.send_keys(password)
        input('Enter to Clock Login Button:')
        lbtn.click()
    def log_out(self):
        input('Enter To Click Menue:')
        menue=self.d.find_element(B.XPATH,"//button[@id='react-burger-menu-btn']")
        menue.click()
        input('Enter To Click LogOut:')
        logout = self.d.find_element(B.XPATH,"//a[@id='logout_sidebar_link']")
        logout.click()
        self.d.quit()

user1=log_inp()
user1.webload()
user1.log_in('standard_user','secret_sauce')
user1.log_out()





