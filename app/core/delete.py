def deletePerson(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    try:
        query = f'DELETE FROM person WHERE aadharCard = {aadharCard};'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteBrand(con, cur):
    brand = input("Brand Name: ")
    try:
        query = f'DELETE FROM brand WHERE brandName = "{brand}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteChannel(con, cur):
    channel = input("Channel Name: ")
    try:
        query = f'DELETE FROM channel WHERE channelName = "{channel}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteShow(con, cur):
    print("Enter the show details: ")
    channel = input("Channel: ")
    date = input("Date: ")
    time = input("Starting Time: ")
    try:
        query = f'DELETE FROM `show` WHERE `date` = "{date}" AND startTime = "{time}" AND channelName = "{channel}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteProduct(con, cur):
    print("Enter the product details: ")
    name = input("Name: ")
    brand = input("Brand Name: ")
    try:
        query = f'DELETE FROM product WHERE `name` = "{name}" AND brandName = "{brand}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteAd(con, cur):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'DELETE FROM production WHERE adSerialNo = {serialNo};'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteGuardian(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    try:
        query = f'DELETE FROM guardianData WHERE aadharCard = {aadharCard};'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteDisplayed(con, cur):
    serialNo = input("Ad Serial No: ")
    print("Enter the show details: ")
    channel = input("Channel: ")
    date = input("Date: ")
    time = input("Starting Time: ")
    try:
        query = f'DELETE FROM displayedBetween WHERE adSerialNo = {serialNo} AND showDate = "{date}" AND showStartTime = "{time}" AND channelName = "{channel}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deletePrefers(con, cur):
    aadhar = input("Actor Aadhar No: ")
    brand = input("Brand Name: ")
    try:
        query = f'DELETE FROM prefers WHERE actorAadharCard = {aadhar} AND brandName = "{brand}";'
        deleted = cur.execute(query)
        if deleted == 0:
            print('\nNo data with given details')
        con.commit()
        print("\nDELETE SUCCESSFULL")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")
