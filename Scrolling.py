from selenium import webdriver
from selenium.webdriver.common.by import By as B

class Scroll:
    def __init__(self):
        self.d=webdriver.Chrome()
    def web_load(self):
        self.d.get('https://www.automationexercise.com/')
        self.d.maximize_window()
    def scroll_point(self):
        input('Enter to Scroll 1000:')
        self.d.execute_script("window.scrollBy(0,1000);")  # Scrolling by point
        print(self.d.execute_script('return window.pageYOffset'))  # For seenig how much scrole done
        input('Enter to Scroll Up 500:')
        self.d.execute_script("window.scrollBy(0,-500);")
        print(self.d.execute_script('return window.pageYOffset'))
    def scrol_elem(self):
        input('Enter To scroll to Half Sleeves Top Schiffli Detailing - Pink Element:')
        elm = self.d.find_element(B.CSS_SELECTOR,"a[href='/product_details/12']")
        self.d.execute_script("arguments[0].scrollIntoView();",elm)
        self.d.execute_script("window.scrollBy(0,-500);")
        input('Enter To click:')
        elm.click()

    def quit_browser(self):
        input('Enter To Quit:')
        self.d.quit()
s1=Scroll()
s1.web_load()
s1.scroll_point()
s1.scrol_elem()
s1.quit_browser()




