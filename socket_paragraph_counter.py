import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl



'''
124 Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML 
document and display the count of the paragraphs as the output of your program. 
Do not display the paragraph text, only count them. Test your program on several
 small web pages as well as some larger web pages”
    
    
    #PREVIOUS PROGRAM

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

https://en.wikipedia.org/wiki/History_of_computing_hardware

https://en.wikipedia.org/wiki/History_of_Python

'''



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikipedia.org/wiki/History_of_Python'
html = urllib.request.urlopen(url, context = ctx).read()

#parse the html
soup = BeautifulSoup(html, 'html.parser')
tags = soup('p')
counts = 0
for tag in tags:
    counts += 1

#paragraphs = soup.find_all(['p', 'div'])
#num_paragraphs = len(paragraphs)
#print(num_paragraphs)

print("The number of paragraphs tags are: ", counts)

