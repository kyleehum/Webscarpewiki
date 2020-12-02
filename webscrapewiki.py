#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:20:40 2020

@author: kylehum
"""

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Mahi-mahi"
page = requests.get(url) 
soup = BeautifulSoup(page.content, 'html.parser') 
print(page)

text_info = BeautifulSoup(page.content, 'html.parser').find_all("p") 
result = text_info[1].text
print(result.strip())
list(text_info)

while True:
    keyword = input("\n\nGreetings, Kyle. What would you like to search? ")
    print(f"\n\nSearching for {keyword}...\n\n")
    try:
        url = f"https://en.wikipedia.org/wiki/{keyword}"
        page = requests.get(url) 
        text_info = BeautifulSoup(page.content, 'html.parser').find_all("p")
        print("This is what I found: \n\n")
        for i in text_info:
           if (i.text != "\n"):
               print(i.text)
               break
        ans = input("\n\nIs this enough, Kyle? ")
        if (ans.strip().lower() == "yes"):
               print("\n\nYou're welcome, Kyle.")
               break
    except:
         print("I am sorry, Kyle. I could not find it.")
    
