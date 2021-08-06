import requests, time, ssl, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

ssl._create_default_https_context = ssl._create_unverified_context

#Static initialized objects
path1 = '/Users/mhisten/OneDrive/Code/scraping/files/Batch/'
path2 = '/Users/mhisten/OneDrive/Code/scraping/files/Batch/Complete'
#path1 = '/home/ubuntu/'


file1 = 'Batch5.txt'
file2 = 'TrueLink5.txt'
link = 'https://en.wikipedia.org/wiki/'
list1 = []
count = 0

os.chdir(path1)
with open(file1, "r") as f:
    Lines = [line for line in f.readlines() if line.strip()]
    for name in Lines:
        count = count + 1
        if count % 10 == 0:
            print(count)
        name = name.replace('|','')
        name = name.strip()
        if '{' in name:
            name = name.replace('{','/')
        
        link1 = link + name

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  
        #chromedriver = '/home/ubuntu/'
        chromedriver = '/Users/mhisten/OneDrive/Code/useful/chromedriver'

        driver = webdriver.Chrome(chromedriver, options=options)

        driver.get(link1)
        time.sleep(1)

        truelink = driver.current_url
        truelink = str(truelink).split('/wiki/')
        #print(truelink[1])
        driver.quit()

        name = str(name + '|')
        if '/' in name:
            name = name.replace('/','{')
        item = str(truelink[1])+'|'
        if '/' in item:
            item = item.replace('/','{')

        outfile = open(path2 + '/' + file2, 'a')
        outfile.write(str(name) + str(item) + '\n')
   

