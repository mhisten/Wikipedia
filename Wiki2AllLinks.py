import os, sys

path1 = '/Users/mhisten/OneDrive/Code/scraping/files/'
path2 = '/Users/mhisten/OneDrive/Code/scraping/files/pagelinks/'
file1 = 'AllLinks0.txt'

#Open all files in folder
os.chdir(path2)
list1 = []
for filename in os.listdir(path2):
    with open(filename, "r") as f:
        if filename != '.DS_Store':
            print(filename)
            #Go line by line
            Lines = [line for line in f.readlines() if line.strip()]
            for line in Lines:
                line = line.strip()
                list1.append(line)
            f.close

#Remove duplicates and save
links = []
[links.append(x) for x in list1 if x not in links]
outfile = open(path1 + '/' + file1, 'a')
for terms in links:
    outfile.write(str(terms) + '\n')
