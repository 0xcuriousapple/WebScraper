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

from bs4 import BeautifulSoup
import re #for regex

#As email are protected by js in vjti website, we have to load page in client side first
#Refer https://stackoverflow.com/questions/56280730/cannot-scrap-protected-email-from-website?noredirect=1&lq=1
#Dynamic Javascript Scraping
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Client(QWebEnginePage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)

        self.html=""
        self.loadFinished.connect(self.on_page_load)

        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.html=self.toHtml(self.Callable)
        print("In on_page_load \n \t HTML: ",self.html)

    def Callable(self,html_str):
        print("In Callable \n \t HTML_STR: ",len(html_str))
        self.html=html_str
        print("In Callable \n \t HTML_STR: ",len(self.html))
        self.app.quit()


url = 'http://www.vjti.ac.in/index.php/academics/civil'
response= Client(url)



html_soup = BeautifulSoup(response.html, 'html.parser')
type(html_soup)
#
faculty_containers = html_soup.find_all('tr', class_ = 'SideBar')
#print(faculty_containers[9])



print(len(faculty_containers))


names = []
Designation = []
Extension = []
Qualification = []
Specialization = []
Email = []

#https://stackoverflow.com/questions/27606265/python-beautifulsoup-extract-text-from-table-cell

# Extract data from individual Faculty container
i=0;
for container in faculty_containers:

    if container.find('img') is not None:
    # The names
        name = container.findAll('td')[3].span.text
        names.append(name)
    # The Designation
        _Designation = container.findAll('td')[1].span.text
        Designation.append(_Designation)
    # The Extension
        _Extension = container.findAll('td')[4].span.text
        Extension.append(_Extension)
    # The Qualification
        _Qualification = container.findAll('td')[5].span.text
        Qualification.append(_Qualification)
    # The Specialization
        _Specialization = container.findAll('td')[6].span.text
        Specialization.append(_Specialization)
    # The Email    
    # Use of regex
        _Email= container.findAll('a',text = re.compile('[\w\.-]+@[\w\.-]+'))[0].text
        Email.append(_Email)
    


                
                
         
import pandas as pd
test_df = pd.DataFrame({'Name': names,
'Designation': Designation,
'Qualification': Qualification,
'Specialization':Specialization,
'Email': Email,
'Extension': Extension
})
print(test_df)
test_df
test_df.to_csv('Civil_Department.csv',encoding='utf-8-sig')




