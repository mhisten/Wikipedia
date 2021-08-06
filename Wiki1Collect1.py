from bs4 import BeautifulSoup
import os, sys, re, csv, codecs, ssl
from urllib.request import urlopen
from urllib.parse import quote

ssl._create_default_https_context = ssl._create_unverified_context

#Static initialized objects
#path1 = '/Users/mhisten/OneDrive/Code/scraping/files/Final/test/'
#path2 = '/Users/mhisten/OneDrive/Code/scraping/files/Final/test/pagelinks'
#path3 = '/Users/mhisten/OneDrive/Code/scraping/files/Final/test/pagecategories'
path1 = '/home/ubuntu/'
path2 = '/home/ubuntu/pagelinks/'
file1 = 'countries.csv'
site = 'https://en.wikipedia.org/wiki/'

#Open document list
f = codecs.open(path1 + file1, 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')
for row in reader:
    name = str(row[0])
    name = quote(name, safe='')
    print(name)

    #Flexible initialized objects
    file3 = name + '.txt'
    list1 = [] #page links

    #Remove irrelevant links
    specific = '_in_' + name.lower()
    bad_words1 = ['help:', 'list_', 'file', 'iso_', 'main_page', 'template', 'special:', 'portal',
    'talk:', 'digital_object', 'wikipedia', 'disambiguation', 'isbn_', 'identifier', 'category:', specific]

    #Open website
    page = urlopen(str(site) + str(name)).read()
    soup = BeautifulSoup(page, "lxml")

    tag = soup.findAll('p') #only take links in text
    for p in tag:
        anchor = p.findAll('a', {'href': re.compile('^/wiki/')})
        for link in anchor:
            find = re.compile('/wiki/(.*?)"') 
            searchItem = re.search(find, str(link))
            item = searchItem.group(1)
            item = str(item)

            #Separate irrelevant links and categories
            if re.compile('|'.join(bad_words1),re.IGNORECASE).search(item.lower()):
                pass
            else:
                list1.append(item)
    
          
    #remove duplicates and save
    links = []
    [links.append(x) for x in list1 if x not in links]

    outfile = open(path2 + '/' + file3, 'a')
    for terms in links:
        outfile.write(str(terms) + '\n')