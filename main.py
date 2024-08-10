import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

file_path = '/Users/rishabhbhartiya/Desktop/IATA/xyz.html'

with open(file_path, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
# Find all rows in the table
rows = soup.find_all('tr')
# Initialize a list to store the scraped data
scraped_data = []
# Iterate through each row
for row in rows:
    # Find all cells in the row
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    scraped_data.append(row_data)
""" Airport = []
Country = []
IATA  = []
for i in scraped_data:
    s = i.split(",")
    Airport.append(s[0])
    Country.append(s[1])
    IATA.append(s[2]) """
    
data = pd.DataFrame(scraped_data, columns=['Airport', 'Country', 'IATA CODE'])
data.to_csv("IATA_XYZ.csv")


