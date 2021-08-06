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
path3 = '/home/ubuntu/pagecategories/'
file1 = 'Batch5.txt'
site = 'https://en.wikipedia.org/wiki/'

#Open document list
count = 0
os.chdir(path1)
with open(file1, "r") as f:
    Lines = [line for line in f.readlines() if line.strip()]
    for name in Lines:
        count = count + 1
        name = name.strip()
        print(str(count) + ' : ' + str(name))

        #Flexible initialized objects
        if '/' in name: 
            name1 = name.replace('/','{')
            file3 = name1 + '.txt'
        else:
            file3 = name + '.txt'
        list1 = [] #page links
        list2 = [] #category links

        #Remove irrelevant links
        specific = '_in_' + name.lower()
        bad_words1 = ['help:', 'list_', 'file', 'iso_', 'main_page', 'template', 'special:', 'portal',
        'talk:', 'digital_object', 'wikipedia', 'disambiguation', 'isbn_', 'identifier', 'category:', specific]
        bad_words2 = ['cs1', 'featured_', 'good_', 'all_', 'coordinates', 'webarchive', 'use_', 'pages_', 'wikidata']
        
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
        
        #Grab categories:
        for link in soup.findAll('a', {'href': re.compile('^/wiki/')}):
            find = re.compile('/wiki/(.*?)"') 
            searchItem = re.search(find, str(link))
            item = searchItem.group(1)
            item = str(item)

            if 'category' in item.lower():
                if re.compile('|'.join(bad_words2),re.IGNORECASE).search(item.lower()):
                    pass
                else:
                    #print(item)
                    item = item.replace('Category:', '')
                    list2.append(item)
                    
        #remove duplicates and save
        links = []
        [links.append(x) for x in list1 if x not in links]
        categories = []
        [categories.append(x) for x in list2 if x not in categories]

        outfile = open(path2 + '/' + file3, 'a')
        for terms in links:
            outfile.write(str(terms) + '\n')
        outfile = open(path3 + '/' + file3, 'a')
        for terms in categories:
            outfile.write(str(terms) + '\n')