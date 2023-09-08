'''“Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) 
displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
Don't worry about the headers for this exercise, 
simply show the first 3000 characters of the document contents.”'''

import urllib.request, urllib.parse, urllib.error

# retrieving the document from a URL
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
count = 0
for line in fhand:
    words = line#.split()
    count = count + len(words) #counting the characters
    if count < 3000:
        print(line.decode().strip())
print('the total number of character is: ', count)