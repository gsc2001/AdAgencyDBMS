import subprocess as sp

from ..core import read, create, delete, update


def add_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============ADD MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n8. Gaurdian\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            create.addActor(connection, cursor)
        elif ch == '2':
            create.addDirector(connection, cursor)
        elif ch == '3':
            create.addBrand(connection, cursor)
        elif ch == '4':
            create.addChannel(connection, cursor)
        elif ch == '5':
            create.addShow(connection, cursor)
        elif ch == '6':
            create.addProduct(connection, cursor)
        elif ch == '7':
            create.addProduction(connection, cursor)
        elif ch == '8':
            create.addGaurdian(connection, cursor)
        else:
            print("Invalid option\n")
        connection.rollback()
        _ = input("Enter a key to continue")


def delete_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============DELETE MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n8. Guardian\n9. Remove Ad from Show\n10. Remove Brand from Actor's preferred brands\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1' or ch == '2':
            delete.deletePerson(connection, cursor)
        elif ch == '3':
            delete.deleteBrand(connection, cursor)
        elif ch == '4':
            delete.deleteChannel(connection, cursor)
        elif ch == '5':
            delete.deleteShow(connection, cursor)
        elif ch == '6':
            delete.deleteProduct(connection, cursor)
        elif ch == '7':
            delete.deleteAd(connection, cursor)
        elif ch == '8':
            delete.deleteGuardian(connection, cursor)
        elif ch == '9':
            delete.deleteDisplayed(connection, cursor)
        else:
            print("Invalid option\n")

        _ = input("Enter a key to continue")


def read_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============READ MENU==================")
        print("0. Back\n1. Get all Actors\n2. Get all Directors\n3. Get all Brands\n4. Get all Channels\n5. Get all Shows\n6. Get all Products\n7. Get all Ads\n8. Get Ad-Show Relations\n9. Get Actor's preferred brands\n10. Get all Guardians\n11. Actors with Physical features\n12. Average ad production cost\n13. Maximum preferred brands\n14. Partial text search for show\n15. Get best shows for an ad\n16. Partial text search for actor\n17. Shows with surcharge less than a value\n18. Maximum of sum of the contract money of brand\n19. Bill for Ad\n20. Shows list by amount\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            read.readActors(connection, cursor)
        elif ch == '2':
            read.readDirectors(connection, cursor)
        elif ch == '3':
            read.readBrands(connection, cursor)
        elif ch == '4':
            read.readChannels(connection, cursor)
        elif ch == '5':
            read.readShows(connection, cursor)
        elif ch == '6':
            read.readProducts(connection, cursor)
        elif ch == '7':
            read.readAds(connection, cursor)
        elif ch == '8':
            read.getAdShows(connection, cursor)
        elif ch == '9':
            read.getActorBrands(connection, cursor)
        elif ch == '10':
            read.getGuardians(connection, cursor)
        elif ch == '11':
            read.actorsByFeatures(connection, cursor)
        elif ch == '12':
            read.avgProduction(connection, cursor)
        elif ch == '13':
            read.maxPreferred(connection, cursor)
        elif ch == '14':
            read.searchShow(connection, cursor)
        elif ch == '15':
            read.showsForAd(connection, cursor)
        elif ch == '16':
            read.searchActor(connection, cursor)
        elif ch == '17':
            read.surchargeLessThan(connection, cursor)
        elif ch == '18':
            read.maxProdCost(connection, cursor)
        elif ch == '19':
            read.adBill(connection, cursor)
        elif ch == '20':
            read.showList(connection, cursor)
        else:
            print("Invalid option\n")

        _ = input("Enter a key to continue")


def update_menu(connection, cursor):
    while True:
        _ = sp.call('clear', shell=True)
        print("==============UPDATE MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n8. Guardian\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            actor_update_menu(connection, cursor)
        else:
            print("Invalid Option\n")


def actor_update_menu(connection, cursor):
    while True:
        _ = sp.call('clear', shell=True)
        print("==============ACTOR UPDATE MENU==================")
        print("0. Back\n1. AccountNumber\n2. Name\n3. Height and Weight\n4. Add preffered brand\n5. Remove preffered brand\n")
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch == '1':
            update.updateAccountNumber(connection, cursor)
        elif ch == '2':
            update.updatePersonName(connection, cursor)
        elif ch == '3':
            update.updateHeightWeight(connection, cursor)
        elif ch == '4':
            create.addPrefers(connection, cursor)
        elif ch == '5':
            delete.deletePrefers(connection, cursor)
        else:
            print("Invalid Option\n")

        _ = input("Enter a key to continue")
