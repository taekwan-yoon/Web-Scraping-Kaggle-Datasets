import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



driver = webdriver.Chrome("/Users/taekwan/Desktop/Web-Scraping-Kaggle-Datasets/webdriver/chromedriver")
driver.get("https://www.kaggle.com/datasets")

driver.maximize_window()  # to see as many elements as possible


time.sleep(2)

box = driver.find_element("xpath","//*[@id='site-content']/div[5]/div/div/div[1]/div/input")

box.send_keys("food")

time.sleep(2)

#calendar_view = driver.find_element("xpath","//*[@id='site-content']/div[6]/div/div/div/div[1]/i[3]")
#calendar_view.click()




#//*[@id="1864"]/div/div[1]/div[1]

# //*[@id="site-content"]/div[6]/div/div/div/ul/li[1]/div[1]/a


#driver.navigate().back()


#driver.find_element("xpath","//*[@id='site-content']/div[5]/div/div/div[1]/div/input").send_keys(Keys.PAGE_DOWN)





time.sleep(2)
print(1)

driver.close()
driver.quit()


