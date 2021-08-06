from bs4 import BeautifulSoup
import os, sys, csv, re, ssl
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context

#paths
#path1 = '/Users/mhisten/OneDrive/Code/scraping/files/'
path1 = '/home/ubuntu/'

#files
file1 = 'Batch5.txt'
file2 = 'WC5.txt'

#web
site = 'https://en.wikipedia.org/wiki/'

count = 0
os.chdir(path1)
with open(file1, "r") as f:
    Lines = [line for line in f.readlines() if line.strip()]
    for name in Lines:
        count = count + 1
        name = name.strip()

        print(str(count) + ' : ' + str(name))

        page = urlopen(str(site) + str(name)).read()
        soup = BeautifulSoup(page, "lxml")

        #take information from paragraphs only
        text = ''
        for paragraph in soup.find_all('p'):
            text += paragraph.text

        #clean html leftovers
        text = re.sub(r'\[.*?\]+', '', text)
        text = text.replace('\n', '')
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')  
        text = text.split(' ')
        cleaned = []
        cleaned = [x for x in text if x.isalpha()]
        
        #Count words
        length = (len(cleaned))
        outfile = open(path1 + file2,'a')
        if '/' in name: 
            name = name.replace('/','{')
        outfile.write(str(name) + '|' + str(length) + '\n')

    f.close