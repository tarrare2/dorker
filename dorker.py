import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.parse
base1 = "https://www." #URL base made
base3 = ".com/search?q="
def menu(): #Menu
    total=0 #Total variable assigned
    listOfLinks=[] #listOfLinks variable assigned
    dorkText = input("Please enter your dork: ") #Parameters of the used dork, amount of pages to search, and used search engine are made
    dork = urllib.parse.quote(dorkText)
    pages = int(input("Number of pages to search: "))
    if pages < 1: #Filters values such as 0 or negative values
        print("Invalid input, please try again.")
        menu()
        return
    #start = (pages-1)*10 
    engineChoice = input("Search with:\n  1)Google\n  2)Bing\n>")
    if engineChoice == "1": 
            base2 = "google"
    elif engineChoice == "2":
            base2 = "bing"
    else: #Filters values that aren't specified i.e. 1 or 2
        print("Please choose a valid number.")
        menu()
        return
    print("########################\nSearching for dork: "+dorkText+" in "+str(pages)+" page(s) of "+base2+"... \n########################") #Notifies the user of their choices
    if base2 == "google":#If you chose google, it uses the start parameter and first if you chose bing
        base4 = "&start="
    else:
        base4="&first="
    for i in range(1,pages+1):
        start=str((i-1)*10)#the start/first parameter takes in 0 for the first page, 10 for the second, 20 for the third, etc. so it converts the chosen number of pages to its respective value
        links,listLength=page((base1+base2+base3),dork , base4, start)#Assigns the list of links and how many there are to 2 variables
        listOfLinks.append(links)#Appends the links to an array
        total += listLength#Adds the value of the amount of links to an integer
    print("\n".join(listOfLinks))# Joins the final list of links
    amount=str(listLength)
    print("************************\nFinished!\nFound "+amount+" dorks!\n************************")#Finishes and alerts you how many links were found

def page(base1to3,dork,base4,start):#Accepts the base URL, chosen dork, page parameter, and page value
    links=[]#Links variable assigned
    headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"}
    request=urllib.request.Request(base1to3+dork+base4+start,headers=headers) #Opens HTTP request to the full URL (e.g.https://www.(b1)google(b2).com/search?q=(b3)inurl:php?id=1(dork)&start=(b4)0(start))
    response=urllib.request.urlopen(request).read()#Requests the webpage's data
    soup = BeautifulSoup(response,"html.parser")#BS4 searches for the links by their attribute
    cited= soup.findAll('cite')#, class_ =True)#For every link, it:
    for i in cited:#For every line with 'cite':
        x=re.sub('<.*?>','',i.text)#Everything except the URL itself is taken out of the line of HTML
        links.append(x)#And appended into an array
    listLength=len(links)#The total length is stored (i.e How many links were found)
    links = '\n'.join(links)#Joins the links into a single string so it can be easily printed
    return links, listLength#Returns the links themselves and how many links have been found
menu()
