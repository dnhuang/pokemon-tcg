import requests
from bs4 import BeautifulSoup
import warnings
import pandas as pd
warnings.filterwarnings('ignore', message='A NumPy version.*"')

# base variables, set to site
base_url = 'https://jp.pokellector.com/'
url = 'https://jp.pokellector.com/Pokemon-151-Expansion/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# get all card numbers and names
soup_elements = soup.find_all(class_='plaque')

# append info into a list
pokemon_list = []
for soup_element in soup_elements:
    curr_list = soup_element.text.split('-')
    pokemon_list.append([curr_list[0][:-1], curr_list[1][1:]])
pokemon_list

# put data into data frame and output
df = pd.DataFrame(pokemon_list, columns=['Set #', 'Name'])
df.to_excel('sv2a.xlsx',index=False)
