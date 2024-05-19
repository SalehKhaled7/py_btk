import time

from selenium import webdriver



driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe') 
# driver = webdriver.Edge('C:/msedgedriver.exe') 

driver.get('https://www.salehkhaled.me/')
time.sleep(10)
print("done waiting")
# Close the browser
driver.quit()

# nice