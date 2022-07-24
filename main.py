from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def get_travel_data(t_name: list, t_address: list):
    state = browser.find_elements(By.CLASS_NAME, 'hfpxzc')

    for i in range(len(state)):
        t_name.append(str(state[i].get_attribute('aria-label')))
        state[i].click()
        time.sleep(3)
        s = browser.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div[3]/span/button')
        t_address.append(str(browser.find_elements(By.CLASS_NAME, 'AeaXub')[0].text))
        s.click()


def save_travel_data(name: list, address: list):
    df = pd.DataFrame([name, address])
    df.to_csv('./a.csv')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.google.co.kr/maps/?hl=ko')
time.sleep(5)

elem = browser.find_element(By.ID, 'searchboxinput')
elem.send_keys('청주 관광지')
browser.implicitly_wait(1)

browser.find_element(By.ID, 'searchbox-searchbutton').click()

name = []
address = []
s = browser.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
for i in range(3):
    time.sleep(3)
    s.send_keys(Keys.PAGE_DOWN)

get_travel_data(name, address)
save_travel_data(name, address)