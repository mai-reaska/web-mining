from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import os
import csv
os.environ['PATH'] += r'C/:SeleniumDriver'
driver = webdriver.Chrome()
driver.get('https://www.boxofficemojo.com/chart/top_lifetime_gross/')
body = driver.find_elements(By.TAG_NAME, 'tbody')
row = driver.find_elements(By.TAG_NAME, 'tr')
with open('web_qtx.csv', mode='w') as file:
    write_file = csv.writer(file)
    for r in row:
        tData = r.find_elements(By.TAG_NAME, 'td')
        row_data = []
        for d in tData:
            row_data.append(d.text)
        write_file.writerow(row_data)
driver.quit()

