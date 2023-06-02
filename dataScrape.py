from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


path =(r'C:\Users\The Luminous\Downloads\chromedriver_win32')
# Write your path here
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'


driver.get(web)

# xpath formst is: //tagName[@attributeName="value"]

matches = driver.find_elements(by='xpath', value= '//tr[@itemprop="name"]')


home = []
score = []
away = []

for match in matches:
    home.append(match.find_element(by='xpath', value='./th[1]').text)
    score.append(match.find_element(by='xpath', value='./th[2]').text)
    away.append(match.find_element(by='xpath', value='./th[3]').text)

dict_football = {'home': home, 'score': score, 'away': away} 
df_football = pd.DataFrame(dict_football) 
df_football['year'] = 1982
time.sleep(2)
driver.quit()

df_football.to_csv("fifa_worldcup_missing_data.csv", index=False)

