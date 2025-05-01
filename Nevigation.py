from selenium import webdriver
from selenium.webdriver.common.by import By as B

class Nevigate:
    def web_nev(self):
        driver = webdriver.Chrome()# Load Webdriver
        driver.get("https://www.automationexercise.com/") #Load Url
        input('Enter to Print:')
        print("URL:",driver.current_url) #Url Printing
        print('Titel',driver.title) # Print Titel
        elt = driver.find_element(B.CSS_SELECTOR,"div[class='item active'] div[class='col-sm-6'] p").text
        print(elt)
        attribute  = driver.find_element(B.XPATH,'//*[@id="slider-carousel"]/div/div[1]/div[1]/a[1]/button').get_attribute('type')
        print(attribute)
        input('Maximizing:')
        driver.maximize_window()
        input('Full Screan:')
        driver.fullscreen_window()
        input('Refersh:')
        driver.refresh()
        input('Go to product:')
        driver.find_element(B.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
        input('Back:')
        driver.back()
        input('Forward:')
        driver.forward()
        input('Minimize:')
        driver.minimize_window()
        input("Quit:")
        driver.quit()
n=Nevigate()
n.web_nev()