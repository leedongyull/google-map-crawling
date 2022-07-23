from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def get_travel_data(t_name: list):
    state = browser.find_elements(By.CLASS_NAME, 'hfpxzc')

    for i in range(len(state)):
        t_name.append(str(state[i].get_attribute('aria-label')))
    
def save_travel_data(name: list):
    df = pd.Series(name)
    df.to_csv('./a.csv')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.google.co.kr/maps/?hl=ko')
time.sleep(5)

elem = browser.find_element(By.ID, 'searchboxinput')
elem.send_keys('청주 관광지')
browser.implicitly_wait(1)

browser.find_element(By.ID, 'searchbox-searchbutton').click()

name = []
for i in range(5):
    get_travel_data(name)
    s= browser.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    s.send_keys(Keys.PAGE_DOWN)

save_travel_data(name)