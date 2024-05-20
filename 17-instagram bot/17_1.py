from selenium import webdriver
from selenium.webdriver.common.by import By
from instagram_info import username,passward
import time


class Instagram():
    def __init__(self,username,passward):
        self.browser = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
        self.username = username
        self.passward = passward
        self.status = False
        self.baseUrl = 'https://instagram.com'

    def login(self):
        self.browser.get(self.baseUrl)
        time.sleep(2)
        username_input = self.browser.find_element(By.NAME,"username")
        username_input.send_keys(self.username)
        password_input = self.browser.find_element(By.NAME,"password")
        password_input.send_keys(self.passward)
        login = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
        login.click()
        self.status = True
        # print(self.status)

    def update_followers_list(self,oldlist  ,newfollowrs):
        for follower in newfollowrs:
            if follower.text not in oldlist:
                oldlist.append(follower.text)
                
                

        return oldlist

    def get_followers(self,user=None, maxusers=100):
        user = user if user else self.username
        self.browser.get(self.baseUrl+'/'+user)
        time.sleep(3)
        
        followers_link = self.browser.find_element(By.XPATH,'(//ul)/li[2]/a')

        followers_link.click()
        time.sleep(3)
        model_div = self.browser.find_element(By.CLASS_NAME,'_aano')
        follower_div = model_div.find_element(By.CSS_SELECTOR,'div')
        
        followers_list = []
        
        # update followr list func 
        last_scroll_position = -1
        # Scroll until the scroll position no longer changes
        while True:
            # Scroll to the bottom of the follower_div
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model_div)


            time.sleep(1.5)  # Wait for scrolling to take effect
            
            # Get the current scroll position
            current_scroll_position = self.browser.execute_script("return arguments[0].scrollTop", model_div)
            
            # Break the loop if the scroll position no longer changes
            if current_scroll_position == last_scroll_position:
                break

            followers = follower_div.find_elements(By.CLASS_NAME,'_ap3a._aaco._aacw._aacx._aad7._aade')
            followers_list = self.update_followers_list(followers_list,followers)
            # print(followers_list)

            # Update the last scroll position
            last_scroll_position = current_scroll_position
            if (len(followers_list) >= maxusers):
                break
        return followers_list
    

    def follow_account(self,acc):
        self.browser.get(self.baseUrl+'/'+acc) # go to user profile
        time.sleep(2)
        follow_btn = self.browser.find_element(By.CSS_SELECTOR,'button') # locae the button

        if follow_btn == "follow" or "follow back":
            follow_btn.click
        
        time.sleep(3)


    def unfollow_account(self,acc):
        self.browser.get(self.baseUrl+'/'+acc) # go to user profile
        time.sleep(2)
        follow_btn = self.browser.find_element(By.CSS_SELECTOR,'button') # locae the button
        
        if follow_btn == "unfollow":
            follow_btn.click
        
        time.sleep(3)


    def save_accs_to_file(self,list):
        with open("followers.txt","w",encoding="UTF-8") as file:
            for f in list:
                file.write(f+'\n')
        print(len(list)+'s users saved to followers.txt')




    


instagram = Instagram(username , passward)


instagram.login()                                       # login to acc
followers = instagram.get_followers('salkhaled71',5)    # get follower list for x user
# instagram.follow_account('acc')                         # follow account
# instagram.unfollow_account('acc')                       # unfollow account


# follower_list=[]
# for follower in followers:
#     follower_list.append(follower)

instagram.save_accs_to_file(followers)                  # save followers to a file



time.sleep(10)
print('closing ...')
instagram.browser.close()






