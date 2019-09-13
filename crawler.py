import pymongo
import requests
import DatabaseManager
import random
import bs4
import validators
import queue
from url_normalize import url_normalize
import re

DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()
workedColl = DBM.getWorkedColl()

workQueue = queue.Queue()


def getRandData():

	print("getting some random data")

	collSize = workColl.count({})
	offset = random.randint(0,collSize-1)

	return (workColl.find({}).limit(20).skip(offset))



def remove(url):

	workColl.remove({'_id':url})


def saveWebColl(tag,url):

	try:

		tag = tag.strip()

		if (tag is None) or (tag is ""):

			return

		webColl.insert_one({'tag':tag,'url':url})

		if workedColl.count_documents({'_id':url},limit = 1) == 0:

			workedColl.insert_one({'_id':url})

	except Exception as ex:

		print("exception@saveWebColl :: ",ex)


def saveWorkColl(url):

	try:

		if workedColl.count_documents({'_id':url},limit = 1) == 0:

			if workColl.count_documents({'_id':url},limit = 1) == 0:

				workColl.insert_one({'_id':url})
				print(" + ",url)

	except Exception as ex:

		print("exception@saveWorkColl ",ex)



def crawlEngine():

	print("@ crawlEngine")

	while True:

		try:

			if workQueue.empty() is True:

				return

			# input("press enter to continue")

			url = url_normalize(workQueue.get())

			if workedColl.count_documents({'_id':url},limit = 1) != 0:

				remove(url)
				continue

			print("@ ",url)

			webPage = requests.get(url).content

			soup = bs4.BeautifulSoup(webPage,'html.parser')

			headings = soup.find_all(re.compile('^h[1-2]$'))

			if soup.title.string is not None:

				saveWebColl(soup.title.string,url)


			for heading in headings:

				saveWebColl(heading.text.strip(),url)



			refList = soup.find_all('a',href=True)

			for link in refList:

				url = url_normalize(link['href'])

				if validators.url(url):

					saveWorkColl(url)

		except Exception as ex:

			print("exception@crawlerEngine ",ex)






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
