''' Searches for input string in data base: https://ndb.nal.usda.gov/ndb/search/list '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import csv, requests, urllib 

def findNutrients(string):
    '''Searches for food and returns dictionary of {nutrients:amount in food in grams or calories}'''
    #Navigate to website and search for food 
    driver = webdriver.Chrome(executable_path=r'C:\Users\nikit\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\common\chromedriver')
    driver.get(r"https:\ndb.nal.usda.gov\ndb\search\list") 
    elem = driver.find_element_by_name("qlookup")
    elem.clear()
    elem.send_keys(string)
    WebDriverWait(driver, 1)
    elem.send_keys(Keys.RETURN)
    
    #Select first entry in list of possible of foods 
    elem = driver.find_element_by_css_selector("#quickform > div.list-left > table > tbody > tr:nth-child(1) > td:nth-child(3) > a") 
    elem.send_keys(Keys.RETURN) 
    WebDriverWait(driver, 1)
      
    #Download CSV file 
    elem = driver.find_element_by_css_selector("body > div.bodywrapper > div.wbox > div > div.menuButton > a:nth-child(7)")
    elem.send_keys(Keys.RETURN) 
    url=str(elem.get_attribute('href')) 
    r = requests.get(url)
    text = r.iter_lines()
    
    #Save nutrient values in dictionary 
    nutrients={}
    l=list()
    d=dict()
    
    for row in text: #generates dictionary with nutrient as key and amount per 100g as value 
        l=(str(row)[2:].replace("'","").replace('"','').split(","))
        if(len(l)>1):
            key=l[0]
            for x in l[1:]:
                try: 
                    value=float(x) 
                    break 
                except (ValueError): value=None
            if(value): d.update({key:value})
            
            
    #elem = None
    return d 