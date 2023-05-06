from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(start_url)

soup = bs(page.text, 'html.parser')

table = soup.find_all('table')
temp_list = []

table_rows = table[7].find_all('tr')

for i in table_rows:
    td_tag = i.find_all('td')
    row = [j.text.rstrip() for j in td_tag]
    temp_list.append(row)
    
Star_names = []
Distance =[]
Mass = []
Radius = []
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

data = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), columns=['Star_names', 'Distance', 'Mass', 'Radius'])
data.to_csv('Dwarf_Stars.csv')