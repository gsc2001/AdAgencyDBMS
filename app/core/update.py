from datetime import date, datetime as dt
import re


def updateAccountNumber(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric() and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    accountNo = input("Account Number: ")
    if len(accountNo) >= 8 and len(accountNo) <= 12 and accountNo.isnumeric() and int(accountNo) > 0:
        accountNo = int(accountNo)
    else:
        print("\nERROR: Please enter valid account number\n")
        return

    try:
        query = f'UPDATE person SET accountNo = {accountNo} WHERE aadharCard = {aadharCard};'
        rows_aff = cur.execute(query)
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updatePersonName(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric() and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    name = input("Name: ")
    if len(name) <= 0:
        print('Please enter name')

    try:
        query = f'UPDATE person SET `name` = "{name}" WHERE aadharCard = {aadharCard};'
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateHeightWeight(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric() and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    height = input("Height in cms: ")
    if height.isnumeric() and int(height) > 0:
        height = int(height)
    else:
        print("\nERROR: Please enter valid Height in cms\n")
        return

    weight = input("Weight in kgs: ")
    if weight.isnumeric() and int(weight) > 0:
        weight = int(weight)
    else:
        print("\nERROR: Please enter valid Weight in kgs\n")
        return

    try:
        query = f'UPDATE actor SET height = {height}, `weight` = {weight} WHERE aadharCard = {aadharCard};'
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSurcharge(con, cur):
    print("Enter the show details: ")
    channel = input("Channel: ")
    try:
        showdate = str(dt.strptime(input("Date in YYYY-MM-DD: "), "%Y-%m-%d"))
    except Exception as e:
        print(e)
        print("\nError: Please enter valid date\n")
        return

    time = input("Starting Time (HH:MM:SS): ")
    try:
        time = str(dt.strptime(time, "%H:%M:%S"))
    except Exception as e:
        print("Please enter a valid time")
        return

    surcharge = input("Enter Surcharge: ")
    if surcharge.isnumeric() and int(surcharge) > 0:
        surcharge = int(surcharge)
    else:
        print("\nERROR: Please enter valid Surcharge\n")
        return

    try:
        query = f"UPDATE `show` SET surcharge = {surcharge} WHERE channelName = '{channel}' AND `date` = '{showdate}' AND startTime = '{time}';"
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateBasePrice(con, cur):
    channel = input("Enter Channel Name: ")
    basePrice = input("Enter baseprice: ")
    if basePrice.isnumeric() and int(basePrice) > 0:
        basePrice = int(basePrice)
    else:
        print("\nERROR: Please enter valid baseprice\n")
        return

    try:
        query = f'UPDATE channel SET basePrice = {basePrice} WHERE channelName = "{channel}";'
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateProductDescription(con, cur):
    print("Enter the product details: ")
    name = input("Product Name: ")
    brand = input("Brand Name: ")
    description = input("Product Description: ")
    if len(description) <= 0:
        description = 'NULL'
    else:
        description = '"' + description + '"'

    try:
        query = f"UPDATE product SET `description` = {description} WHERE `name` = '{name}' AND brandName = '{brand}';"
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateProductPrice(con, cur):
    print("Enter the product details: ")
    name = input("Product Name: ")
    brand = input("Brand Name: ")
    price = input("Product price: ")
    if price.isnumeric() and int(price) > 0:
        price = int(price)
    try:
        query = f"UPDATE product SET price = {price} WHERE `name` = '{name}' AND brandName = '{brand}';"
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSalary(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric() and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    salary = input("Salary: ")
    if salary.isnumeric() and int(salary) >= 10000:
        salary = int(salary)
    else:
        print("\nERROR: Please enter valid salary abive 10000\n")
        return

    try:
        query = f'UPDATE director SET salary = {salary} WHERE aadharCard = {aadharCard};'
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateSupervisor(con, cur):
    aadharCard = input("12 digit Aadhar Card: ")
    if len(aadharCard) == 12 and aadharCard.isnumeric() and int(aadharCard) > 0:
        aadharCard = int(aadharCard)
    else:
        print("\nERROR: Please enter valid aadhar card\n")
        return

    supAadharCard = input("12 digit Supervisor Aadhar Card: (Enter for none)")
    if supAadharCard == "":
        supAadharCard = "NULL"
    elif len(supAadharCard) == 12 and supAadharCard.isnumeric() and int(supAadharCard) > 0 and int(supAadharCard) != int(aadharCard):
        supAadharCard = int(supAadharCard)
    else:
        print("\nERROR: Please enter valid Supervisor Aadhar Card\n")
        return

    try:
        query = f'UPDATE director SET supervisorAadharCard = {supAadharCard} WHERE aadharCard = {aadharCard};'
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")

    return


def updateBrandEmail(con, cur):
    print("Enter the brand details: ")
    brand = input("Enter Brand Name: ")
    email = input("Email: ")
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, email):
        print("\nError: Please enter a valid Email Id\n")
        return

    try:
        query = f"UPDATE brand SET pocEmail = '{email}' WHERE brandName = '{brand}';"
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")


def updateBrandPhone(con, cur):
    print("Enter the brand details: ")
    brand = input("Enter Brand Name: ")
    phone = input("Phone: ")
    if phone.isnumeric() and len(phone) == 10 and int(phone) > 0:
        phone = int(phone)
    else:
        print("\nError: Please enter a valid Phone Number\n")
        return

    try:
        query = f"UPDATE brand SET `pocPhone` = {phone} WHERE brandName = '{brand}';"
        rows_aff = cur.execute(query)
        print(f'{rows_aff} rows changed!')
        con.commit()
        if rows_aff == 0:
            print("\nNothing was updated\n")
        else:
            print("\nUPDATE SUCCESSFULL\n")
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: UPDATE FAILED!\n")
