
import sys, os, re

path1 = '/Users/mhisten/OneDrive/Code/scraping/files/'
path2 = '/Users/mhisten/OneDrive/Code/scraping/files/pagelinks/'
file1 = 'LC.txt'


list1 = []
count1 = 0

os.chdir(path2)
for filename in os.listdir(path2):
    with open(filename, "r") as f:
        if filename != '.DS_Store':
            count1 = count1 + 1
            print(str(count1) + ' : ' + filename)
            Lines = [line for line in f.readlines() if line.strip()]
            count = 0
            for name in Lines:
                count = count + 1

            item = str(filename + '|' + str(count))
            list1.append(item)
            
            f.close()

outfile = open(path1 + '/' + file1, 'a')
for terms in list1:
    outfile.write(str(terms) + '\n')