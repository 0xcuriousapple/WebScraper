# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:25:28 2020

@author: TheHead
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:22:00 2020

@author: TheHead
"""

from requests import get
from bs4 import BeautifulSoup
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
from warnings import warn
url = 'http://www.vjti.ac.in/index.php/academics/civil'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
#
faculty_containers = html_soup.find_all('tr', class_ = 'SideBar')
print(faculty_containers[9])
print(len(faculty_containers))


names = []
Designation = []
Extension = []
Qualification = []
Specialization = []
Email = []
https://stackoverflow.com/questions/27606265/python-beautifulsoup-extract-text-from-table-cell

# Extract data from individual movie container
for container in faculty_containers:
# If the movie has Metascore, then extract:
    if container.find('img') is not None:
    # The name
        name = container.h3.a.text
        names.append(name)
    # The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
    # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
    # The Metascore
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))
    # The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))
    


                
                
     """           
import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(test_df)
test_df
test_df.to_csv('example.csv')"""