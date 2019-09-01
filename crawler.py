import pymongo import requests import DatabaseManager import random 
import bs4 import validators import queue from url_normalize import 
url_normalize

DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()

workQueue = queue.Queue()


def getRandData():

	print("getting some random data")

	collSize = workColl.count({})
	offset = random.randint(0,collSize-1)

	return (workColl.find({}).limit(20).skip(offset))

def sanitizeURL():

	retu

def crawlEngine():

	print("@ crawlEngine")

	while True:

		if workQueue.empty() is True:

			return

		url = workQueue.get()
		print("@ ",url)

		soup = bs4.BeautifulSoup(requests.get(url).content,'html.parser')
		refList = soup.find_all('a',href=True)

		for link in refList:

			url = url_normalize(link['href'])

			if validators.url(url):

				try:

					workColl.insert_one({'_id':url})
					print(" + ",url)
				
				except Exception as ex:

					print(ex)



def main():

	print("crawler is ready")

	while True:

		print("@ main")

		if workQueue.empty() is True:

			urlList = getRandData()

			for i in urlList:

				workQueue.put(i['_id'])

		crawlEngine()



main()
