import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date
import re


def updateAccountNumber(cur, con):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    accountNo = input("Account Number: ")
    if len(accountNo) >= 8 and len(accountNo) <= 12 and accountNo.isnumeric and int(accountNo) > 0:
        accountNo = int(accountNo)
    else:
        print("\nERROR: Please enter valid account number\n")
        return

    try:
        query = f'UPDATE person SET accountNo = {accountNo} WHERE aadharCard = {aadharCard};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateHeightWeight(cur, con):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    height = input("Height in cms: ")
    if height.isnumeric and int(height) > 0:
        height = int(height)
    else:
        print("\nERROR: Please enter valid Height in cms\n")
        return

    weight = input("Weight in kgs: ")
    if weight.isnumeric and int(weight) > 0:
        weight = int(weight)
    else:
        print("\nERROR: Please enter valid Weight in kgs\n")
        return

    try:
        query = f'UPDATE actor SET height = {height}, `weight` = {weight} WHERE aadharCard = {aadharCard};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSurcharge(cur, con):
    print("Enter the show details: ")
    channel = input("Channel: ")
    try:
        showdate = date(input("Date in YYYY-MM-DD: "))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid date\n")

    time = input("Starting Time: ")
    regex = '(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'
    if not re.search(regex, time):
        print("\nError: Please enter a valid start time in HH-MM-SS format\n")
        return

    surcharge = input("Enter Surcharge: ")
    if int(surcharge) > 0:
        surcharge = int(surcharge)
    else:
        print("\nERROR: Please enter valid Surcharge\n")
        return

    try:
        query = f"UPDATE `show` SET surcharge = {surcharge} WHERE channelName = '{channel}' AND `date` = {showdate} AND startTime = {time}"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateBasePrice(cur, con):
    channel = input("Enter Channel Name: ")
    basePrice = input("Enter baseprice: ")
    if int(basePrice) > 0:
        basePrice = int(basePrice)
    else:
        print("\nERROR: Please enter valid baseprice\n")
        return

    try:
        query = f'UPDATE channel SET basePrice = {basePrice} WHERE channelName = {channel};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateProductDescription(cur, con):
    print("Enter the product details: ")
    name = input("Product Name: ")
    brand = input("Brand Name: ")
    description = input("Product Description: ")
    if description == "":
        description = "NULL"
    try:
        query = f"UPDATE product SET `description` = {description} WHERE `name` = '{name}' AND brandName = '{brand}'"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSalary(cur, con):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    salary = input("Salary: ")
    if salary.isnumeric and int(salary) >= 10000:
        salary = int(salary)
    else:
        print("\nERROR: Please enter valid salary abive 10000\n")
        return

    try:
        query = f'UPDATE director SET salary = {salary} WHERE aadharCard = {aadharCard};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSupervisor(cur, con):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    supAadharCard = input("12 digit Supervisor Aadhar Card: ")
    if supAadharCard == "":
        supAadharCard = "NULL"
    elif len(supAadharCard) == 12 and supAadharCard.isnumeric and int(supAadharCard) > 0 and int(supAadharCard) != int(aadharCard):
        supAadharCard = int(supAadharCard)
    else:
        print("\nERROR: Please enter valid Supervisor Aadhar Card\n")
        return

    try:
        query = f'UPDATE director SET supervisorAadharCard = {supAadharCard} WHERE aadharCard = {aadharCard};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return
