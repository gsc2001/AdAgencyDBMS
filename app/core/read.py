from tabulate import tabulate

def printResult(cur):
    result = cur.fetchall()

    if len(result) != 0:
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate(rows, header, tablefmt = 'grid'))
    else:
        print("No Data!")

def readBrands(con, cur):
    try:
        query = 'SELECT * FROM brand;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readActors(con, cur):
    try:
        query = 'SELECT * FROM actor NATURAL JOIN person NATURAL JOIN phone;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readDirectors(con, cur):
    try:
        query = 'SELECT * FROM director NATURAL JOIN person NATURAL JOIN phone;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readChannels(con, cur):
    try:
        query = 'SELECT * FROM channel;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readShows(con, cur):
    try:
        query = 'SELECT * FROM `show`;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readProducts(con, cur):
    try:
        query = 'SELECT * FROM product;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readAds(con, cur):
    try:
        query = 'SELECT production.*, duration FROM production INNER JOIN ad ON ad.serialNo = production.adSerialNo;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def getAdShows(con, cur):
    try:
        query = 'SELECT * FROM displayedBetween;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def getActorBrands(con, cur):
    try:
        query = 'SELECT actorAadharCard AS `Actor Aadhar Card`, GROUP_CONCAT(brandName) AS `Preferred Brands` FROM prefers GROUP BY actorAadharCard;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def getGuardians(con, cur):
    try:
        query = 'SELECT guardianData.*, GROUP_CONCAT(guardian.jActorAadharCard) AS `Actor Aadhar Cards` FROM guardian NATURAL JOIN guardianData GROUP BY aadharCard;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def maxProdCost(con, cur):
    try:
        query = 'SELECT MAX(TotalCost.NetCost) AS `Highest Production Cost` FROM (SELECT SUM(production.productionCost) AS NetCost FROM production INNER JOIN product ON ( product.name = production.productName AND product.brandName = production.brandName ) GROUP BY product.brandname) AS TotalCost;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def adBill(con, cur):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'SELECT production.productionCost + COALESCE(SUM(channel.basePrice) + SUM(displayedBetween.timesShown * ad.duration * `show`.surcharge),0) AS Bill FROM (((( displayedBetween RIGHT JOIN ad ON displayedBetween.adSerialNo = ad.serialNo) LEFT JOIN `show` ON displayedBetween.showDate = `show`.date AND displayedBetween.showStartTime = `show`.startTime AND displayedBetween.channelName = `show`.channelName) LEFT JOIN production ON ad.serialNo = production.adSerialNo) LEFT JOIN `channel` ON `show`.channelName = channel.channelName) WHERE ad.serialNo = {serialNo};'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def showList(con, cur):
    try:
        query = 'SELECT (`show`.surcharge * SUM(ad.duration)) AS Earning, `show`.date, `show`.startTime, `show`.channelName, `show`.name FROM (( displayedBetween INNER JOIN ad ON displayedBetween.adSerialNo = ad.serialNo) INNER JOIN `show` ON displayedBetween.showDate = `show`.date AND displayedBetween.showStartTime = `show`.startTime AND displayedBetween.channelName = `show`.channelName) GROUP BY `show`.date, `show`.startTime, `show`.channelName, `show`.name ORDER BY Earning DESC;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def actorsByFeatures(con, cur):
    print("Enter physical features range: ")
    minHeight = input("Minimum Height (in cm): ")
    maxHeight = input("Maximum Height (in cm): ")
    minWeight = input("Minimum Weight (in kg): ")
    maxWeight = input("Maximum Weight (in kg): ")
    gender = input('Gender (Male or Female or Other):')
    try:
        query = f'SELECT * FROM person INNER JOIN actor ON person.aadharCard = actor.aadharCard WHERE person.gender = "{gender}" AND ( actor.height BETWEEN {minHeight} AND {maxHeight} ) AND ( actor.weight BETWEEN {minWeight} AND {maxWeight} );'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def avgProduction(con, cur):
    try:
        query = 'SELECT AVG(productionCost) FROM production;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def maxPreferred(con, cur):
    try:
        query = 'SELECT brandname, COUNT(brandname) AS count_prefer FROM prefers GROUP BY brandname ORDER BY count_prefer DESC LIMIT 1;'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def searchShow(con, cur):
    text = input("Enter part of name: ")
    try:
        query = f'SELECT date, startTime, channelName, name FROM `show` WHERE name like "%{text}%";'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def searchActor(con, cur):
    text = input("Enter part of name: ")
    try:
        query = f'SELECT actor.aadharCard AS AadharCard, name FROM person INNER JOIN actor ON person.aadharCard = actor.aadharCard WHERE person.name like "%{text}%"'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def surchargeLessThan(con, cur):
    maxSurcharge = input("Enter part of name: ")
    try:
        query = f'SELECT name AS showName FROM `show` WHERE `show`.surcharge < {maxSurcharge};'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def showsForAd(con, cur):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'SELECT showDate, showStartTime, channelName FROM showGenre WHERE name IN (SELECT name As AdGenrename FROM ad INNER JOIN adGenre on serialNo = adSerialNo WHERE serialNo = {serialNo});'
        cur.execute(query)
        printResult(cur)
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")
