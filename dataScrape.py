from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


path =(r'C:\Users\The Luminous\Downloads\chromedriver_win32')
# Write your path here
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)




def get_missing_year(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

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

    dict_football = {'home': home, 'score': score, 'away': away, 'year':year} 
    df_football = pd.DataFrame(dict_football) 
    time.sleep(2)
    # df_football.to_csv("fifa_worldcup_missing_data_{year}.csv", index=False)
    return df_football


years =  [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018,2022]

fifa = [ get_missing_year(year) for year in years]

driver.quit()

print(fifa)
df_fifa = pd.concat (fifa, ignore_index=True, join='inner')
print(df_fifa)
df_fifa.to_csv("fifa_worldcup_missing_datas.csv", index=False)



