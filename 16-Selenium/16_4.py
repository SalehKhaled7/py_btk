from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')

driver.get("https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

all_products = driver.find_element(By.ID, "1")
time.sleep(2)

titles=all_products.find_elements(By.TAG_NAME,"h3")
time.sleep(2)

for title in titles:
    print(title.text)

time.sleep(5)