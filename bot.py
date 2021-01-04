from time import sleep
from selenium import webdriver

class Instabot:
    def __init__(self, username, password):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/p/a").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")\
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(password)
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(4)
      
        
    def get_unfollow(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,'following')]")\
            .click()
        sleep(1)
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
          
   #     sug=self.driver.find_element_by_xpath('//h4[contains(text(),Suggestions)]')
    #    self.driver.execute_script('arguments[0].scrollIntoView()', sug)
        sleep(1)
   #     last_height = self.driver.execute_script("return document.body.scrollHeight")
       
        
        while True:
         
    # Scroll down to bottom
           buttons = self.driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
           for btn in buttons:
    # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
              
              
              self.driver.execute_script("arguments[0].click();", btn)
    # Wait to load page
          
              sleep(1)
           self.driver.execute_script("window.scrollBy(0,5000)","")
       
username_1=input("enter user name : ") 
pass_1=input("enter password : ")   
df=Instabot(username_1,pass_1 )
          
df.get_unfollow()
