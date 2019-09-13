import pymongo

class DatabaseManager:

	__instanceRef = None

	def __init__(self):

		self.db = pymongo.MongoClient("mongodb://localhost:27017/")['TinySearch']

		self.workColl = self.db['workColl']
		self.searchColl = self.db['searchColl']
		self.imgColl = self.db['imgColl']
		self.wikiColl = self.db['wikiColl']
		self.webColl = self.db['webColl']
		self.workedColl = self.db['workedColl']

		DatabaseManager.__instanceRef = self



	def getDatabaseManager():

		if DatabaseManager.__instanceRef is None:

			DatabaseManager()

		return DatabaseManager.__instanceRef


	def getDB(self):

		return self.db


	def getWorkColl(self):

		return self.workColl

	def getSearchColl(self):

		return self.searchColl

	def getImgColl(self):

		return self.imgColl

	def getWikiColl(self):

		return self.wikiColl

	def getWebColl(self):

		return self.webColl

	def getWorkedColl(self):

		return self.workedColl
