import subprocess as sp
import pymysql
import pymysql.cursors
import re


def deletePerson(cur, con):
    aadharCard = input("12 digit Aadhar Card: ")
    try:
        query = f'DELETE FROM person WHERE aadharCard = {aadharCard}'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteBrand(cur, con):
    brand = input("Brand Name: ")
    try:
        query = f'DELETE FROM brand WHERE brandName = \'{brand}\''
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteChannel(cur, con):
    channel = input("Channel Name: ")
    try:
        query = f'DELETE FROM channel WHERE brandName = \'{channel}\''
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteShow(cur, con):
    print("Enter the show details: ")
    channel = input("Channel: ")
    date = input("Date: ")
    time = input("Starting Time: ")
    try:
        query = f'DELETE FROM show WHERE date = \'{date}\' AND startTime = \'{time}\' AND channelName = \'{channel}\''
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteProduct(cur, con):
    print("Enter the product details: ")
    name = input("Name: ")
    brand = input("Brand Name: ")
    try:
        query = f'DELETE FROM product WHERE name = \'{name}\' AND brandName = \'{brand}\''
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")


def deleteAd(cur, con):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'DELETE FROM production WHERE adSerialNo = {serialNo}'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: DELETE FAILED!\n")
