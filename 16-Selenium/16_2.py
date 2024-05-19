# selenoum basics
from selenium import webdriver
import time 

def take_screenshot():
    page_title = driver.title.replace(" ","_")
    driver.save_screenshot(f"{page_title}_{int(time.time())}.png") # take a screenshot

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get('https://google.com')


# time.sleep(2)             # stop here for 2 sec
driver.maximize_window()    # full screen the browser
print(driver.title)         # get page title

driver.maximize_window()    # full screen the browser
# take_screenshot()

time.sleep(2)
driver.get('https://hepsiburada.com')
# take_screenshot()

time.sleep(5)
driver.back()               # go back 1 page
driver.back()               # go back 1 page
# driver.forward()          # go forward 1 page


time.sleep(2)
print("closing")

driver.close()