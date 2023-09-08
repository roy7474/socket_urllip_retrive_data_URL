'''“Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) 
displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
Don't worry about the headers for this exercise, 
simply show the first 3000 characters of the document contents.”'''

import urllib.request, urllib.parse, urllib.error
count = 0
# Testing side link: http://data.pr4e.org/romeo-full.txt
user_file = input('Enter the URL of the website that you would like to use: ')
try:
    fhand =urllib.request.urlopen(user_file) # retrieving the document from a URL
    
except:
    print("There was an error while trying to open this file. Please try again! ")

for line in fhand:
    words = line#.split()
    count = count + len(words) #counting the characters
    if count < 3000:
        print(line.decode().strip()) #displaying only 3000 characters
print('The total number of character is:', count)