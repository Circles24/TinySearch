import pymongo
import DatabaseManager
import validators

DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()

currColl = None

def line():
	print("**********************************")


def collChoice():

	line()
	print("           SELECT COLLECTION           \n")
	print("1  ::   workColl                         ")
	print("2  ::   searchColl                       ")
	print("3  ::   wikiColl                         ")
	print("4  ::   webColl                          ")
	print("5  ::   imgColl                          ")
	print("6  ::   exit                             ")
   
	return int(input())

def opChoice():

	line()
	print("         SELECT OPERATION              \n")
	print("1  ::   view                             ")
	print("2  ::   feed                             ")
	print("3  ::   wipe                             ")
	print("4  ::   remove                           ")
	print("5  ::   exit                             ")

	return int(input())



def menu():

	while(True):


		try:

			choice = collChoice()

			if choice is 1:

				currColl = workColl


			elif choice is 2:

				currColl = searchColl


			elif choice is 3:

				currColl = wikiColl


			elif choice is 4:

				currColl = webColl


			elif choice is 5:

				currColl = webColl

			elif choice is 6:

				break


			else :

				continue

			
			choice = opChoice()

			if choice is 1: #view

				elemList = currColl.find({})

				if currColl is workColl:

					for i in elemList:

						print("# ")
						print(i['_id'])


			if choice is 2: #feed

				if currColl is workColl:

					url = input("enter the url to be fed")

					if validators.url(url) is True:

						workColl.insert_one({'_id':url})
					
					else :

						print("you entered wrong url")

				if currColl is wikiColl:

					tag = input("enter the tag")
					url = input("enter the wiki url")
					title = input("enter the wiki title")

					if validators.url(url) is True:

						workColl.insert_one({'_id':tag, 'title':title, 'url':url  })
					
					else :
						print("you entered wrong url")

				if currColl is webColl:

					tag = input("enter the tag")
					url = input("enter the web url")
					title = input("enter the web title")

					if validators.url(url) is True:

						webColl.insert_one({'_id':tag, 'title':title, 'url':url  })
					
					else :
						print("you entered wrong url")



			elif choice is 3: #wipe

				currColl.drop()


			elif choice is 4: #remove

				print("choice is 4")
			
			elif choice is 5:

				print("choice is 5")




		except Exception as ex:

			print("wrong data entered")
			print(ex)

menu()
