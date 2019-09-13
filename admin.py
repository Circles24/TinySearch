import pymongo
import getpass
import os
import DatabaseManager
import feed
import reporter

DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()
workedColl = DBM.getWorkedColl()

def line():
    print('\n******************************************\n')
def hline():
    print("________________________________________________")

def authenticate():

    print("Authentication Underway")

    tries = 0
    open("admin.txt","r")


    f = open("admin.txt","r")
    AdminPass = f.read().strip()
    f.close()


    while(True):

        user_pass = getpass.getpass(prompt='Password: ', stream=None)

        if AdminPass == user_pass:

            print("Sucessful Verification")
            break

        print("Wrong Password")
        print(tries+1," Wrong Attempts")
        tries+=1

        if(tries > 5):

            print("Better Luck Next Time")
            return False

    return True


def innerMenu():

    line()
    print("                 ADMIN MENU               \n")
    print("1  ::  View workColl                         ")
    print("2  ::  View workedColl                       ")
    print("3  ::  View wikiColl                         ")
    print("4  ::  View searchColl                       ")
    print("5  ::  View imgColl                          ")
    print("6  ::  View webColl                          ")
    print("7  ::  Wipe whole Database                   ")
    print("8  ::  Feed test data                        ")
    print("9  ::  Get Stat Report                       ")
    print("10 ::  Change Password                       ")
    print("11 ::  exit                                  ")


    choice = input()

    try:
        choice = int(choice)

    except ValueError:

        print("wrong input")
        return 0

    if choice < 0 or choice > 11:
        print("wrong input")
        return 0

    return  choice

def menu():

    choice = 0

    while(choice == 0):
        choice = innerMenu()

    line()

    if choice is 1:

        workCollList = workColl.find({})

        for data in workCollList:

            print(data['_id'])

        print("been there done that")

    elif choice is 2:

        workedCollList = workedColl.find({})

        for data in workedCollList:

            print(data['_id'])


    elif choice is 3:

        wikiCollList = wikiCollList.find({})

        for data in wikiCollList:

            print(data['_id'])

    elif choice is 4:

        searchCollList = searchColl.find({})

        for data in searchCollList:

            print(data['_id'])

    elif choice is 5:

        searchCollList = searchColl.find({})

        for data in SearchCollList:

            print(data['_id'])

    elif choice is 6:

        webCollList = webColl.find({})

        for data in webCollList:

            print(data['tag']," ")

    elif choice is 7:

        print("continue to wipe database (1/0) ")

        choice = int(input())

        if choice == 1:

            workColl.drop()
            workedColl.drop()
            wikiColl.drop()
            searchColl.drop()
            imgColl.drop()
            webColl.drop()

            print("your whole database is wiped")

        else :

            return True

    elif choice is 8:

        feed.menu()

    elif choice is 9:

        reporter.report()

    elif choice is 10:

        newPass1 = getpass.getpass(prompt='New Password: ', stream=None)
        newPass2 = getpass.getpass(prompt='Repeat New Password',stream=None)

        if newPass1 == newPass2:

            f = open('admin.txt','w+')
            f.write(newPass1)
            f.close()

            print("Password changed successfully")

        else:

            print("both password dont match")

    else:
        return False

    line()

    return True

def main():

    print("@ main")

    print("Welcome Admin")
    if authenticate() is False:

        print("Bye")
        return

    while(True):
        if menu() is False:
            break

    print("Have a nice day Admin")


main()
