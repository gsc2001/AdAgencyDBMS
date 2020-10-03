import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date
import re


def addDirector():
    global cur
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
        row["DOB"] = date(input("Date of Birth in YYYY-MM-DD: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Date of Birth\n")

    # row["age"] = date.today.year - row['DOB'].year - \
    #     ((date.today.month, date.today.day) <
    #      (row['DOB'].month, row['DOB'].day))

    row["salary"] = input("Salary: ")
    if row["salary"].isnumeric() and row["salary"] > 0:
        row["salary"] = int(row["salary"])
    else:
        print("\nError: Please enter valid Salary\n")
        return

    try:
        row["joinDate"] = date(input("Date of Joining in YYYY-MM-DD: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid Date of Joining\n")

    row["supervisorAadharCard"] = input("12 digit Supervisor AadharCard: ")
    if len(row["supervisorAadharCard"]) == 12 and row["supervisorAadharCard"].isnumeric():
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
        query = "INSERT INTO person(aadharCard, name, accountNo, gender, DOB) VALUES('%d', '%s', '%d', '%s', '%s')" % (
            row["aadharCard"], row["name"], row["accountNo"], row["galary"], row["DOB"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    try:
        query = "INSERT INTO director(aadharCard, joinDate, salary, supervisorAadharCard) VALUES('%d', '%s', '%d', '%d')" % (
            row["aadharCard"], row["joinDate"], row["salary"], row["supervisorAadharCard"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    for i in range(num_phone):
        try:
            query = "INSERT INTO phone(aadharCard, phoneNo) VALUES('%d', '%d')" % (
                row["aadharCard"], row_phone[i])
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return
    return


def addActor():
    global cur
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
        row["DOB"] = date(input("Date of Birth in YYYY-MM-DD: "))
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
        query = "INSERT INTO person(aadharCard, name, accountNo, gender, DOB) VALUES('%d', '%s', '%d', '%s', '%s')" % (
            row["aadharCard"], row["name"], row["accountNo"], row["galary"], row["DOB"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    try:
        query = "INSERT INTO actor(aadharCard, experience, height, weight) VALUES('%d', '%d', '%d', '%d')" % (
            row["aadharCard"], row["experience"], row["height"], row["weight"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

    for i in range(num_phone):
        try:
            query = "INSERT INTO phone(aadharCard, phoneNo) VALUES('%d', '%d')" % (
                row["aadharCard"], row_phone[i])
            cur.execute(query)
            con.commit()
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
            query = "INSERT INTO juniorActor(aadharCard) VALUES('%d')" % (
                row["aadharCard"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
            print("\nError: PLEASE TRY AGAIN!\n")
            return

        for i in range(num_guard):
            try:
                query = "INSERT INTO guardian(jActorAadharCard, aadharCard) VALUES('%d', '%d')" % (
                    row["aadharCard"], row_guardians[i][1])
                cur.execute(query)
                con.commit()
            except Exception as e:
                con.rollback()
                print(e)
                print("\nError: PLEASE TRY AGAIN!\n")
                return

            try:
                query = "INSERT INTO guardianData(aadharCard, name, phone) VALUES('%d', '%s', '%d')" % (
                    row_guardians[i][1], row_guardians[i][2], row_guardians[i][0])
                cur.execute(query)
                con.commit()
            except Exception as e:
                con.rollback()
                print(e)
                print("\nError: PLEASE TRY AGAIN!\n")
                return
    return


def addBrand():
    global cur
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
        query = "INSERT INTO brand(brandName, email, phone) VALUES('%s', '%s', '%d')" % (
            row["brandName"], row["email"], row["phone"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return


def addChannel():
    global cur
    row = {}

    row["channelName"] = input("Enter Channel Name: ")
    row["baseprice"] = input("Baseprice: ")
    if row["baseprice"] > 0:
        print("\nError: Please enter a valid Baseprice\n")
        return
    try:
        query = "INSERT INTO brand(channelName, baseprice) VALUES('%s', '%d')" % (
            row["channelName"], row["baseprice"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return


def addPrefers():
    global cur
    row = {}

    row["brandName"] = input("Enter Brand Name: ")
    row["actorAadharCard"] = input("actorAadharCard: ")
    if len(row["aadharCard"]) == 12 and row["aadharCard"].isnumeric():
        row["aadharCard"] = int(row["aadharCard"])
    else:
        print("\nError: Please enter valid 12 digit Actor Aadhar Card Number\n")
        return
    
    try:
        query = "INSERT INTO prefers(actorAadharCard, brandName) VALUES('%d', '%s')" % (
            row["actorAadharCard"], row["brandName"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return

def addProduct():
    global cur
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
        query = "INSERT INTO product(name, brandName, description, price) VALUES('%s', '%s', '%s', '%d')" % (
            row["name"], row["brandName"], row["description"], row["price"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: PLEASE TRY AGAIN!\n")
        return