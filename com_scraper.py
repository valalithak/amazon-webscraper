import urllib2
import csv
import string
import sys
import os
from string import replace
from bs4 import BeautifulSoup
import requests

title = []
writer = []
rating = []
site = []
price = []
num_reviews = []
final = []

#random_var = 0

def scrap ( soup ):
        #for i in soup:
            name = soup.find("div",{"class":"p13n-sc-truncate p13n-sc-line-clamp-1"})
		    #print name.string.strip() + ";"
            #Title = name.text.strip()
            title.append(name.text.strip())
            print name.string.strip()

            author = soup.find("div",{"class":"a-row a-size-small"})
            Writer = author.string.strip()
		    #print author.string.strip() + ";"
            writer.append(author.string.strip())

            ratings = soup.find("span",{"class":"a-icon-alt"})
            #avg_rating = ratings.a.i.find("span",{"class":"a-icon-alt"})
            #print avg_rating.string.strip() + ";"
            #Rating = avg_rating.text.encode("UTF8")
            print ratings.text.encode("UTF8")
            rating.append(ratings.text.encode("UTF8"))

            n = soup.find("a",{"class":"a-size-small a-link-normal"})
            #review = n.find("a",{"class":"a-size-small a-link-normal"})
            #print review.string.strip() + ";"
            #Review_count = review.string.strip()
            print n.text.strip()
            num_reviews.append(n.text.strip())

            #money = i.find("div", { "class":"zg_itemImmersion"})
            #money1 = money.

            main = "https://www.amazon.in"
            link = soup.find("a",{"class": "a-link-normal"})
            url = main + link['href']
            print url
            site.append(url)

            pr = soup.find("span",{"class" : "p13n-sc-price"})
            print pr.text.strip()
            price.append(pr.text.strip())


def scrape(soup):
    for st in soup.find_all("div",{"class":"zg_itemWrapper"}):
        scrap(st)

for i in range(1,6):
    #var1 ="https://www.amazon.in/gp/bestsellers/books/#"

    url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#" + str(i)
    print url
    #new = urllib2.urlopen(url)
    new = requests.get(url)
    soup = BeautifulSoup(new.content,"html.parser")
    #alll= soup.find_all("div",{"class":"zg_itemWrapper"})
    scrape(soup)

for i in range(0,100):
	temp = [title[i], site[i], writer[i], num_reviews[i], rating[i]]
    #print temp
	final.append(temp)

final.append(["Name", "URL", "Author", "Number of Ratings", "Average"])

os.system('mkdir output && touch output/com_book.csv')
f = open('output/com_book.csv','w')

#with open('output/in_book.csv','w') as file:
#	x = csv.writer(file)
#for i in final:
#    x.writerow(i)
x = csv.writer(f)
for i in final:
	x.writerow(i)
