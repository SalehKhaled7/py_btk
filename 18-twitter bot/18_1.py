from user_info import loging_info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class XBot():
    def __init__(self):
        self.browser = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
        self.username = loging_info.username
        self.password = loging_info.passward
        self.baseUrl = 'https://x.com'
        self.isLogged = False


    def login(self):
        self.browser.maximize_window()
        self.browser.get(self.baseUrl+'/login')
        time.sleep(7)
        username_input = self.browser.find_element(By.NAME,'text')
        username_input.send_keys(self.username)
        time.sleep(1)
        next_btn = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
        next_btn.click()
        time.sleep(1)
        # pass_input = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pass_input = self.browser.switch_to.active_element
        pass_input.send_keys(self.password)
        time.sleep(1)
        # login_btn = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
        pass_input.send_keys(Keys.RETURN)
        
    def search(self,search_key):
        search_input = self.browser.find_element(By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')
        search_input.send_keys(search_key)
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)

        time.sleep(3)
        articl_count = 0
        while True:
            
            body = self.browser.find_element(By.TAG_NAME,'body')
            body.send_keys(Keys.SPACE)
            time.sleep(0.5) 

            search_timeline_elements = self.browser.find_elements(By.XPATH, "//article[@data-testid='tweet']")
            
            articl_count = len(search_timeline_elements)
            if articl_count >= 5:
                for index, article in enumerate(search_timeline_elements):
                    tweet_text = article.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]')
                    retweets = article.find_element(By.CSS_SELECTOR,'button[data-testid="retweet"]')
                    like = article.find_element(By.CSS_SELECTOR,'button[data-testid="like"]')
                    print(index + 1, tweet_text.text)
                    print(f"retweets: {retweets.text} - likes:{like.text}")
                    print('-----------------')
                    time.sleep(0.1)
            break

            # Update article count
            

        


xbot = XBot()

xbot.login()
time.sleep(5)
xbot.search('gpt4o')
time.sleep(10)
print('closing...')
xbot.browser.close()


