

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:22:00 2020

@author: TheHead
"""
"""
Failed Attempt :
	 I was trying to generalize web scraping to all departments, but they all don't have common semantics.
	 So for each department one will have to write different scrapper as each department page have a different structure.
	 for example 
	 Order of columns in table: Designation is first in civil while the name is first in comp
	 There is no column for a photo in comp
	 Specialisation in electrical is written as Specialization in civil and [MS]Specialization in comp
	 Extension in Civil and Electrical is written as Phone in Comp
	 We can solve this naming conflict by hard-coding but there are conflicts in the structure of HTML too
	 Content in <span> in civil while in <p> for electrical.
	 and many more...
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


url = 'http://www.vjti.ac.in/index.php/academics/electrical'
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


pos_of_column = {

}
for container in faculty_containers:
    #print(container.find('strong'))
  
    if str(container.find('strong')) == "<strong>Sr. No.<br/></strong>":
           i=0; 
           for element in container.findAll('td'):
                   print(element.strong.text)
                   pos_of_column[element.strong.text]=i
                   i=i+1
           break
           

print(pos_of_column)

for container in faculty_containers:

    if container.find('a',text = re.compile('[\w\.-]+@[\w\.-]+')) is not None:
    # The names
        name = container.findAll('td')[pos_of_column['Name']].span.text
        names.append(name)
    # The Designation
        _Designation = container.findAll('td')[pos_of_column['Designation']].span.text
        Designation.append(_Designation)
    # The Extension
        _Extension = container.findAll('td')[pos_of_column['Extension']].span.text
        Extension.append(_Extension)
    # The Qualification
        _Qualification = container.findAll('td')[pos_of_column['Qualification']].span.text
        Qualification.append(_Qualification)
    # The Specialization
        pos=0
        if 'Specialization' in pos_of_column : pos= pos_of_column['Specialization']
        if 'Specialisation' in pos_of_column : pos= pos_of_column['Specialisation']
        _Specialization = container.findAll('td')[pos].span.text
        Specialization.append(_Specialization)
    # The Email    
        _Email= container.findAll('a',text = re.compile('[\w\.-]+@[\w\.-]+'))[0].text
        print( container.findAll('a',text = re.compile('[\w\.-]+@[\w\.-]+'))[0].text)
        print(container.findAll('a')[0].text)
    
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
#test_df.to_csv('example.csv',encoding='utf-8-sig')


def Clean_String(test_string ):
    bad_chars = ['Â']  
    for i in bad_chars : 
        test_string = test_string.replace(i, '') 
    return test_string
