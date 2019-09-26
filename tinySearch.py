import re
import sanitizer
import DatabaseManager


DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
workedColl = DBM.getWorkedColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()

def search(searchQuery):

    print("inside search method")
    print("Query :: ",searchQuery)

    searchQueryList = searchQuery.split()
    searchQueryList = sanitizer.filter(searchQueryList);

    res = []
    priRes = []

    print("# ",len(searchQueryList))

    for word in searchQueryList:

    	newWord = '.*'+word+'.*'

    	regQ = re.compile(newWord,re.IGNORECASE)

    	lis = webColl.find({'tag':{'$regex':regQ}})

    	for i in lis:

    		res.append((i['tag'],i['url']))

    res = list(dict.fromkeys(res))

    for entity in res:

    	pri = 0

    	for query in searchQueryList:

    		pri += int((bool(query in entity[0])))

    	priRes.append((pri,entity[0],entity[1]))

    priRes = sorted(priRes, reverse=True)

    res = []

    for entity in priRes:

    	res.append((entity[1],entity[2]))

    return res
