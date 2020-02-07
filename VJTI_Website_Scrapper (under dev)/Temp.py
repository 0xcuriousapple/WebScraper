# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:20:34 2020

@author: TheHead
"""

import requests
from bs4 import BeautifulSoup

def web(page,WebUrl):
     if(page>0):
          url = WebUrl
          code = requests.get(url)
          plain = code.text
          s = BeautifulSoup(plain, "html.parser")
          for link in s.findAll('a', {'class':'s-access-detail-page'}):
               tet = link.get('title')
               print(tet)
               tet_2 = link.get('href')
               print(tet_2)

web(1,'https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles')