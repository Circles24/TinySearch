import pymongo
import DatabaseManager


DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()
workedColl = DBM.getWorkedColl()


def line():
    print('\n******************************************\n')

def getChoice():

    line()
    print("       REPORT MENU         ")
    print()

    print("1 :: Database Report")
    print("2 :: workColl Report")
    print("3 :: workedColl Report")
    print("4 :: wikiColl Report")
    print("5 :: searchColl Report")
    print("6 :: imgColl Report")
    print("7 :: webColl Report")
    print("8 :: Exit")

    choice = int(input())

    if choice < 1 or choice > 8:

        return 0

    return choice

def report():

    currColl = ""

    while True:

        try:

            choice = 0
            while choice == 0:
                choice = getChoice()

                if choice == 0:
                    print("wrong choice")

            if choice == 8:
                print("towards salvation")

                return

            elif choice == 1:

                DBProperties = DBM.getDB().command("dbstats")
                print( 'db            :: ',DBProperties['db'] )
                print( 'collections   :: ',DBProperties['collections'] )
                print( 'views         :: ',DBProperties['views'] )
                print( 'total objects :: ',DBProperties['objects'] )
                print( 'avg obj size  :: ',DBProperties['avgObjSize'] )
                print( 'dataSize      :: ',DBProperties['dataSize'] )
                print( 'numExtents    :: ',DBProperties['numExtents'] )
                print( 'indexes       :: ',DBProperties['indexes'] )
                print( 'indexSize     :: ',DBProperties['indexSize'] )
                print( 'fsTotalSize   :: ',DBProperties['fsTotalSize'] )
                # print(DBProperties) // for further details

            elif choice == 2:

                currColl = "workColl"

            elif choice == 3:

                currColl = "workedColl"

            elif choice == 4:

                currColl = "wikiColl"

            elif choice == 5:

                currColl = "searchColl"

            elif choice == 6:

                currColl = "imgColl"

            elif choice == 7:

                currColl = "webColl"

            if choice != 1:

                properties = DBM.getDB().command("collstats", currColl)

                print( 'ns            :: ',properties['ns'] )
                print( 'size          :: ',properties['size'] )
                print( 'count         :: ',properties['count'] )
                print( 'avg obj size  :: ',properties['avgObjSize'] )
                print( 'storageSize   :: ',properties['dataSize'] )


        except Exception as ex:

            print("Exception@Reporter.report() :: ",ex)
