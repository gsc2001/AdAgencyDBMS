import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date
import re


def addDirector(cur, con):
    row = {}
    print("Enter the new director's details: ")

    row["aadharCard"] = input("12 digit AadharCard: ")
    if len(row["aadharCard"]) == 12 and row["aadharCard"].isnumeric():
        row["aadharCard"] = int(row["aadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Aadhar Card Number\n")
        return

    row["name"] = input("Name: ")
    if len(row["name"]) <= 0:
        print("\nError: Please enter a name\n")
        return

    row["accountNo"] = input("Account Number: ")
    if len(row["accountNo"]) >= 8 and len(row["accountNo"]) <= 12 and row["accountNo"].isnumeric():
        row["accountNo"] = int(row["accountNo"])
    else:
        print("\nError: Please enter valid Account Number\n")
        return

    row["gender"] = input("Male / Female / Other: ")
    if row["gender"] != "Male" and row["gender"] != "Female" and row["gender"] != "Other":
        print("\nError: Please enter valid gender\n")
        return

    try:
        row["DOB"] = str(date(input("Date of Birth in YYYY-MM-DD: ")))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Date of Birth\n")

    age = date.today.year - row['DOB'].year - \
        ((date.today.month, date.today.day) <
         (row['DOB'].month, row['DOB'].day))

    if age < 18:
        print("\nError: Very young director. Minimum age is 18\n")
        return

    row["salary"] = input("Salary: ")
    if row["salary"].isnumeric() and row["salary"] >= 10000:
        row["salary"] = int(row["salary"])
    else:
        print("\nError: Please enter valid Salary above 10000\n")
        return

    try:
        row["joinDate"] = input("Date of Joining in YYYY-MM-DD: ")
        if row["joinDate"] == "":
            row["joinDate"] = str(date.today())
        else:
            row["joinDate"] = str(date(row["joinDate"]))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Date of Joining\n")

    row["supervisorAadharCard"] = input("12 digit Supervisor AadharCard: ")
    if len(row["supervisorAadharCard"]) == 12 and row["supervisorAadharCard"].isnumeric() and row["supervisorAadharCard"] != row["aadharCard"]:
        row["supervisorAadharCard"] = int(row["supervisorAadharCard"])
    elif row["supervisorAadharCard"] == "":
        row["supervisorAadharCard"] = "NULL"
    else:
        print("\nError: Please enter valid 12 digit Supervisor Aadhar Card Number\n")
        return

    row_phone = []
    try:
        num_phone = int(input("Number of director's phone number: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter a valid number\n")
    for i in range(num_phone):
        phone = input("Phone Number: ")
        if phone.isnumeric() and phone > 0 and len(phone) == 10:
            phone = int(phone)
            row_phone.append(phone)
        else:
            print("\nError: Please enter valid 10 digit Phone Number\n")
            return

    try:
        query = "INSERT INTO person(aadharCard, name, accountNo, gender, DOB) VALUES(%d, '%s', %d, '%s', '%s');" % (
            row["aadharCard"], row["name"], row["accountNo"], row["galary"], row["DOB"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    try:
        query = "INSERT INTO director(aadharCard, joinDate, salary, supervisorAadharCard) VALUES(%d, '%s', %d, %d);" % (
            row["aadharCard"], row["joinDate"], row["salary"], row["supervisorAadharCard"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    for i in range(num_phone):
        try:
            query = "INSERT INTO phone(aadharCard, phoneNo) VALUES(%d, %d);" % (
                row["aadharCard"], row_phone[i])
            cur.execute(query)
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    
    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addActor(cur, con):
    row = {}
    print("Enter the new actor's details: ")

    row["aadharCard"] = input("12 digit AadharCard: ")
    if len(row["aadharCard"]) == 12 and row["aadharCard"].isnumeric():
        row["aadharCard"] = int(row["aadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Aadhar Card Number\n")
        return

    row["name"] = input("Name: ")
    if len(row["name"]) <= 0:
        print("\nError: Please enter a name\n")
        return

    row["accountNo"] = input("Account Number: ")
    if len(row["accountNo"]) >= 8 and len(row["accountNo"]) <= 12 and row["accountNo"].isnumeric():
        row["accountNo"] = int(row["accountNo"])
    else:
        print("\nError: Please enter valid Account Number\n")
        return

    row["gender"] = input("Male / Female / Other: ")
    if row["gender"] != "Male" and row["gender"] != "Female" and row["gender"] != "Other":
        print("\nError: Please enter valid gender\n")
        return

    try:
        row["DOB"] = str(date(input("Date of Birth in YYYY-MM-DD: ")))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Date of Birth\n")

    age = date.today.year - row['DOB'].year - \
        ((date.today.month, date.today.day) <
         (row['DOB'].month, row['DOB'].day))

    row["experience"] = input("Experience in Years: ")
    if row["experience"].isnumeric() and row["experience"] > 0 and row["experience"] < age:
        row["experience"] = int(row["experience"])
    else:
        print("\nError: Please enter valid Experience\n")
        return

    row["height"] = input("Height in cms: ")
    if row["height"].isnumeric() and row["height"] > 0:
        row["height"] = int(row["height"])
    else:
        print("\nError: Please enter valid Height\n")
        return

    row["weight"] = input("weight in kgs: ")
    if row["weight"].isnumeric() and row["weight"] > 0:
        row["weight"] = int(row["weight"])
    else:
        print("\nError: Please enter valid Weight\n")
        return

    row_phone = []
    try:
        num_phone = int(input("Number of actor's phone number: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter a valid number\n")
    for i in range(num_phone):
        phone = input("Phone Number: ")
        if phone.isnumeric() and phone > 0 and len(phone) == 10:
            phone = int(phone)
            row_phone.append(phone)
        else:
            print("\nError: Please enter valid 10 digit Phone Number\n")
            return

    try:
        query = "INSERT INTO person(aadharCard, name, accountNo, gender, DOB) VALUES(%d, '%s', %d, '%s', '%s');" % (
            row["aadharCard"], row["name"], row["accountNo"], row["galary"], row["DOB"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    try:
        query = "INSERT INTO actor(aadharCard, experience, height, weight) VALUES(%d, %d, %d, %d);" % (
            row["aadharCard"], row["experience"], row["height"], row["weight"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    for i in range(num_phone):
        try:
            query = "INSERT INTO phone(aadharCard, phoneNo) VALUES(%d, %d);" % (
                row["aadharCard"], row_phone[i])
            cur.execute(query)
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return

    if(age < 18):
        row_guardians = []
        try:
            num_guard = int(input("Number of actor's guardians: "))
        except Exception as e:
            print(e)
            print("\nError: Please enter a valid number\n")
        for i in range(num_guard):
            name = input("Name of Guardian: ")
            phone = input("Phone Number of Guardian: ")
            aadharCard = input("Aadhar Card of Guardian: ")
            if phone.isnumeric() and phone > 0 and len(phone) == 10 and len(aadharCard) == 12 and aadharCard > 0 and aadharCard.isnumeric() and len(name) > 0:
                phone = int(phone)
                aadharCard = int(aadharCard)
                row_guardians.append([phone, aadharCard, name])
            else:
                print("\nError: Please enter valid details\n")
                return

        try:
            query = "INSERT INTO juniorActor(aadharCard) VALUES(%d);" % (
                row["aadharCard"])
            cur.execute(query)
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return

        for i in range(num_guard):
            try:
                query = "INSERT INTO guardian(jActorAadharCard, aadharCard) VALUES(%d, %d);" % (
                    row["aadharCard"], row_guardians[i][1])
                cur.execute(query)
            except Exception as e:
                con.rollback()
                print(e)
                print("\nError: PLEASE TRY AGAIN!\n")
                return

            try:
                query = "INSERT INTO guardianData(aadharCard, name, phone) VALUES(%d, '%s', %d);" % (
                    row_guardians[i][1], row_guardians[i][2], row_guardians[i][0])
                cur.execute(query)
            except Exception as e:
                con.rollback()
                print(e)
                print("\nError: PLEASE TRY AGAIN!\n")
                return

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addBrand(cur, con):
    row = {}

    row["brandName"] = input("Enter Brand Name: ")
    row["email"] = input("Email: ")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, row["email"]):
        print("\nError: Please enter a valid Email Id\n")
        return
    row["phone"] = input("Phone: ")
    if (not row["phone"].isnumeric()) or len(row["phone"]) != 10:
        print("\nError: Please enter a valid Phone Number\n")
        return
    try:
        query = "INSERT INTO brand(brandName, email, phone) VALUES('%s', '%s', %d);" % (
            row["brandName"], row["email"], row["phone"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addChannel(cur, con):
    row = {}

    row["channelName"] = input("Enter Channel Name: ")
    row["baseprice"] = input("Baseprice: ")
    if row["baseprice"] > 0:
        print("\nError: Please enter a valid Baseprice\n")
        return
    try:
        query = "INSERT INTO brand(channelName, baseprice) VALUES('%s', %d);" % (
            row["channelName"], row["baseprice"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addPrefers(cur, con):
    row = {}

    row["brandName"] = input("Enter Brand Name: ")
    row["actorAadharCard"] = input("actorAadharCard: ")
    if len(row["aadharCard"]) == 12 and row["aadharCard"].isnumeric():
        row["aadharCard"] = int(row["aadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Actor Aadhar Card Number\n")
        return

    try:
        query = "INSERT INTO prefers(actorAadharCard, brandName) VALUES(%d, '%s');" % (
            row["actorAadharCard"], row["brandName"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addProduct(cur, con):
    row = {}

    row["brandName"] = input("Enter Brand Name: ")
    row["name"] = input("Enter Product Name: ")
    row["description"] = input("Enter Product description: ")
    if row["description"] == "":
        row["description"] = "NULL"
    row["price"] = input("Enter price: ")
    if row["price"] < 0 or (not row["price"].isnumeric):
        print("\nError: Please enter valid price\n")
        return
    else:
        row["price"] = int(row["price"])

    try:
        query = "INSERT INTO product(name, brandName, description, price) VALUES('%s', '%s', '%s', %d);" % (
            row["name"], row["brandName"], row["description"], row["price"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addProduction(cur, con):
    row = {}

    row["brandName"] = input("Enter Brand Name: ")
    row["productName"] = input("Enter Product Name: ")
    row["actorAadharCard"] = input(
        "Enter Aadhar Card of actor working in that Ad: ")
    if len(row["actorAadharCard"]) == 12 and row["actorAadharCard"].isnumeric():
        row["actorAadharCard"] = int(row["actorAadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Actor Aadhar Card Number\n")
        return
    row["directorAadharCard"] = input(
        "Enter Aadhar Card of director working in that Ad: ")
    if len(row["directorAadharCard"]) == 12 and row["directorAadharCard"].isnumeric():
        row["directorAadharCard"] = int(row["directorAadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Actor Director Card Number\n")
        return

    try:
        row["signingDate"] = input("Enter Signing Date of Ad in YYYY-MM-DD: ")
        if row["signingDate"] == "":
            row["signingDate"] = str(date.today())
        else:
            row["signingDate"] = str(date(row["signingDate"]))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Signing Date\n")

    row["productionCost"] = input("Enter Production Cost of Ad: ")
    if row["productionCost"] > 0 and row["productionCost"].isnumeric:
        row["productionCost"] = int(row["productionCost"])
    else:
        print("\nError: Please enter valid Production Cost\n")
        return

    row["duration"] = input("Enter Duration of Ad in sec: ")
    if row["duration"] > 0 and row["duration"].isnumeric:
        row["duration"] = int(row["duration"])
    else:
        print("\nError: Please enter valid duration\n")
        return

    row_genre = []
    genre_list = ['Comedy', 'Thriller', 'Romance',
                  'Suspense', 'Sci-fi', 'Action', 'Horror', 'Fantasy']
    try:
        num_genre = int(input("Number of genre in Ad: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter a valid number\n")
    for i in range(num_genre):
        name = input(
            "Genre from Comedy|Thriller|Romance|Suspense|Sci-fi|Action|Horror|Fantasy: ")
        if name in genre_list:
            row_genre.append(name)
        else:
            print("\nError: Please enter valid genre\n")
            return

    try:
        query = "INSERT INTO production(actorAadharCard, directorAadharCard, productName, brandName, signingDate, productionCost) VALUES(%d, %d, '%s', '%s', '%s', %d);" % (
            row["actorAadharCard"], row["directorAadharCard"], row["productName"], row["brandName"], row["signingDate"], row["productionCost"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    adId = cur.lastrowid

    try:
        query = "INSERT INTO ad(serialNo, duration) VALUES(%d, %d);" % (
            adId, row["duration"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    for i in range(num_genre):
        try:
            query = "INSERT INTO adGenre(name, adSerialNo) VALUES('%s', %d);" % (
                row_genre[i], adId)
            cur.execute(query)
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addShow(cur, con):
    row = {}

    row["name"] = input("Enter Show Name: ")
    row["channelName"] = input("Enter Channel Name on which show is aired: ")
    row["startTime"] = input("Enter Start Time of show in HH-MM-SS: ")
    regex = '(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'
    if not re.search(regex, row["startTime"]):
        print("\nError: Please enter a valid start time in HH-MM-SS format\n")
        return
    try:
        row["date"] = str(
            date(input("Enter Air Date of Show in YYYY-MM-DD: ")))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Airing Date\n")

    row["duration"] = input("Enter Duration of Show in min: ")
    if row["duration"] > 0 and row["duration"].isnumeric:
        row["duration"] = int(row["duration"])
    else:
        print("\nError: Please enter valid duration\n")
        return

    row["surcharge"] = input("Enter Surcharge of Show: ")
    if row["surcharge"] > 0 and row["surcharge"].isnumeric:
        row["surcharge"] = int(row["surcharge"])
    else:
        print("\nError: Please enter valid surcharge\n")
        return

    row_genre = []
    genre_list = ['Comedy', 'Thriller', 'Romance',
                  'Suspense', 'Sci-fi', 'Action', 'Horror', 'Fantasy']
    try:
        num_genre = int(input("Number of genre in Show: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter a valid number\n")
    for i in range(num_genre):
        name = input(
            "Genre from Comedy|Thriller|Romance|Suspense|Sci-fi|Action|Horror|Fantasy: ")
        if name in genre_list:
            row_genre.append(name)
        else:
            print("\nError: Please enter valid genre\n")
            return

    try:
        query = "INSERT INTO show(date, startTime, channelName, duration, surcharge, name) VALUES('%s', '%s', '%s', %d, %d, '%s');" % (
            row["date"], row["startTime"], row["channelName"], row["duration"], row["surcharge"], row["name"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    for i in range(num_genre):
        try:
            query = "INSERT INTO showGenre(name, showDate, showStartTime, channelName) VALUES('%s', '%s', '%s', '%s');" % (
                row_genre[i], row["date"], row["startTime"], row["channelName"])
            cur.execute(query)
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addAdinShow(cur, con):
    row = {}

    row["adSerialNo"] = input("Please enter Serial number of Ad: ")
    if row["adSerialNo"].isnumeric and row["adSerialNo"] > 0:
        row["adSerialNo"] = int(row["adSerialNo"])
    else:
        print("\nError: Please enter a valid serial Number\n")
        return

    row["channelName"] = input("Enter Channel Name on which show is aired: ")
    row["startTime"] = input(
        "Enter Start Time of show in HH-MM-SS on which Ad is to be displayed: ")
    regex = '(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'
    if not re.search(regex, row["startTime"]):
        print("\nError: Please enter a valid start time in HH-MM-SS format\n")
        return

    try:
        row["date"] = str(
            date(input("Enter Air Date of Show in YYYY-MM-DD: ")))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Airing Date\n")

    row["timesShown"] = input(
        "Please enter number of times Ad is shown during Show: ")
    if row["timesShown"].isnumeric and row["timesShown"] > 0:
        row["timesShown"] = int(row["timesShown"])
    elif row["timesShown"] == "":
        row["timesShown"] = 1
    else:
        print("\nError: Please enter a valid number\n")
        return

    try:
        query = "INSERT INTO displayedBetween(showDate, showStartTime, channelName, adSerialNo, timesShown) VALUES('%s', '%s', '%s', %d, %d);" % (
            row["showDate"], row["showStartTime"], row["channelName"], row["adSerialNo"], row["timesShown"])
        cur.execute(query)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")

    try:
        con.commit()
    except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return
