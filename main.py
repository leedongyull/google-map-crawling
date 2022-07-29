from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def get_input_data(name: str):
    input_data = pd.read_csv('./input/' + name + '.csv').transpose()
    return list(input_data.iloc[0])

def search_country(name: str):
    browser.get('https://www.google.co.kr/maps/?hl=ko')
    time.sleep(1)

    elem = browser.find_element(By.ID, 'searchboxinput')
    elem.send_keys(name + ' 관광지')
    time.sleep(1)

    browser.find_element(By.ID, 'searchbox-searchbutton').send_keys(Keys.ENTER)

def get_travel_data(t_name: list, t_address: list):
    state = browser.find_elements(By.CLASS_NAME, 'hfpxzc')

    for i in range(len(state)):
        t_name.append(str(state[i].get_attribute('aria-label')))
        state[i].send_keys(Keys.ENTER)
        time.sleep(1)

        t_address.append(str(browser.find_elements(By.CLASS_NAME, 'AeaXub')[0].text))
        time.sleep(1)

    browser.get('https://www.google.co.kr/maps/?hl=ko')

def save_travel_data(name: list, address: list, f_name: str):
    df = pd.DataFrame([name, address]).transpose()
    df.to_csv('./output/' + f_name + '.csv')


browser = webdriver.Chrome(ChromeDriverManager().install())
entire_name = get_input_data('한국행정구역')

for i, x in enumerate(entire_name):
    detail_name = get_input_data(x)

    for j, y in enumerate(detail_name):
        name = []
        address = []

        if x == '광역시': search_country(y)
        else : search_country(x + ' ' + y)

        time.sleep(1)
        s = browser.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
        for i in range(3):
            time.sleep(1)
            s.send_keys(Keys.PAGE_DOWN)

        get_travel_data(name, address)
        save_travel_data(name, address, x + '_' + y)