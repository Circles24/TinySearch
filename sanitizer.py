import re
from nltk.corpus import stopwords

stopwordsList = stopwords.words("english")

def sanitize(str):

	str = str.strip()
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

	for i in str:
		if i == ' ':
			raise Exception("wrong string provided") 

	if( regex.search(str) == None):

		return str

	raise Exception("Wrong string provided")

def canBeRemoved(word):


	if word in stopwordsList:

		return True

	return False


def filter(wordList):

	tempList = []

	for word in wordList:

		print("   ",word,"  ",canBeRemoved(word))

		if canBeRemoved(word) is False:


			tempList.append(word)
			

	returnList = []

	for word in tempList:

		try:

			returnList.append(sanitize(word))

		except Exception as ex:

			print("exception@sanitizer.filter :: ",ex)

	return returnList

while True:

	str = input("enter the word to be sanitize\n")

	if str == "exit":
		break

	print(filter(str.split()))
	# print(canBeRemoved(str))
