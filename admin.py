import pymongo
import getpass
import os
import DatabaseManager
import feed

DBM = DatabaseManager.DatabaseManager.getDatabaseManager()

workColl = DBM.getWorkColl()
wikiColl = DBM.getWikiColl()
imgColl = DBM.getImgColl()
webColl = DBM.getWebColl()
searchColl = DBM.getSearchColl()

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
    print("2  ::  View searchColl                       ")
    print("3  ::  View wikiColl                         ")
    print("4  ::  View webColl                          ")
    print("5  ::  View imgColl                          ")
    print("6  ::  Wipe whole Database                   ")
    print("7  ::  Feed test data                        ")
    print("8  ::  Get Stat Report                       ")
    print("9  ::  Change Password                       ")
    print("10 ::  exit                                  ")


    choice = input()

    try:
        choice = int(choice)

    except ValueError:

        print("wrong input")
        return 0

    if choice < 0 or choice > 8:
        print("wrong input")
        return 0

    return  choice

def menu():

    choice = 0

    while(choice == 0):
        choice = innerMenu()

    line()

    if choice is 1:

        email_list = email_coll.find({})
        for email in email_list:

            print(email['_id'],end=' ')
            print(trackerdb.command("collstats", email['_id'])['count'],"\n")

    elif choice is 2:

        email_list = email_coll.find({})

        for email in email_list:

            print('\n',email['_id'])
            hline()

            user_coll = trackerdb[email['_id']]
            user_url_list = user_coll.find({})

            for url in user_url_list:
                print('\n',url['url'])

            hline()


    elif choice is 3:

        usr_email = input("enter the email of the user\n")

        exists = False

        temp_list = email_coll.find({'_id':usr_email})
        for i in temp_list:
            exists = True

        if exists is True:

            usr_coll = trackerdb[usr_email]
            url_list = usr_coll.find({})

            for url in url_list:
                print('\n',url['url'])

        else :

            print("wrong user")

    elif choice is 4:

        os.system("python3 clean_db.py")

    elif choice is 5:

        os.system("python3 feed_db.py")

    elif choice is 6:

        stats_list = trackerdb['stats'].find({})

        for stat in stats_list:
            print('\n',stat['name']," ",stat["count"])

    elif choice is 7:

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

    print("Welcome Admin")
    if authenticate() is False:

        print("Bye")
        return

    while(True):
        if menu() is False:
            break

    print("Have a nice day Admin")
# main()

innerMenu()
