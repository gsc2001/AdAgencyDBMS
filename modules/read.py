def readBrands(cur, con):
    try:
        query = 'SELECT * FROM brand;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readActors(cur, con):
    try:
        query = 'SELECT * FROM actor NATURAL JOIN person NATURAL JOIN phone;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readDirectors(cur, con):
    try:
        query = 'SELECT * FROM director NATURAL JOIN person NATURAL JOIN phone;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readChannels(cur, con):
    try:
        query = 'SELECT * FROM channel;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readShows(cur, con):
    try:
        query = 'SELECT * FROM `show`;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readProducts(cur, con):
    try:
        query = 'SELECT * FROM product;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def readAds(cur, con):
    try:
        query = 'SELECT production.*, duration FROM production INNER JOIN ad ON ad.serialNo = production.adSerialNo;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def maxProdCost(cur, con):
    try:
        query = 'SELECT MAX(TotalCost.NetCost) AS HighestProductionCost FROM (SELECT SUM(production.productionCost) AS NetCost FROM production INNER JOIN product ON ( product.name = production.productName AND product.brandName = production.brandName ) GROUP BY product.brandname) AS TotalCost;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def adBill(cur, con):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'SELECT production.productionCost + SUM(channel.basePrice) + SUM(displayedBetween.timesShown * ad.duration * `show`.surcharge) AS Bill FROM (((( displayedBetween INNER JOIN ad ON displayedBetween.adSerialNo = ad.serialNo) INNER JOIN `show` ON displayedBetween.showDate = `show`.date AND displayedBetween.showStartTime = `show`.startTime AND displayedBetween.channelName = `show`.channelName) INNER JOIN production ON ad.serialNo = production.adSerialNo) INNER JOIN channel ON `show`.channelName = channel.channelName) WHERE displayedBetween.adSerialNo = {serialNo};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def showList(cur, con):
    try:
        query = 'SELECT (`show`.surcharge * SUM(ad.duration)) AS Earning, `show`.date, `show`.startTime, `show`.channelName, `show`.name FROM (( displayedBetween INNER JOIN ad ON displayedBetween.adSerialNo = ad.serialNo) INNER JOIN `show` ON displayedBetween.showDate = `show`.date AND displayedBetween.showStartTime = `show`.startTime AND displayedBetween.channelName = `show`.channelName) GROUP BY `show`.date, `show`.startTime, `show`.channelName, `show`.name ORDER BY Earning DESC;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def actorsByFeatures(cur, con):
    print("Enter physical features range: ")
    minHeight = input("Minimum Height (in cm): ")
    maxHeight = input("Maximum Height (in cm): ")
    minWeight = input("Minimum Weight (in kg): ")
    maxWeight = input("Maximum Weight (in kg): ")
    gender = input('Gender (Male or Female or Other):')
    try:
        query = f'SELECT * FROM person INNER JOIN actor ON person.aadharCard = actor.aadharCard WHERE person.gender = "{gender}" AND ( actor.height BETWEEN {minHeight} AND {maxHeight} ) AND ( actor.weight BETWEEN {minWeight} AND ${maxWeight} );'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def avgProduction(cur, con):
    try:
        query = 'SELECT AVG(productionCost) FROM production;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def maxPreferred(cur, con):
    try:
        query = 'SELECT brandname, COUNT(brandname) AS count_prefer FROM prefers GROUP BY brandname ORDER BY count_prefer DESC LIMIT 1;'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def searchShow(cur, con):
    text = input("Enter part of name: ")
    try:
        query = f'SELECT date, startTime, channelName, name FROM `show` WHERE name like "%{text}%";'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def searchActor(cur, con):
    text = input("Enter part of name: ")
    try:
        query = f'SELECT actor.aadharCard AS AadharCard, name FROM person INNER JOIN actor ON person.aadharCard = actor.aadharCard WHERE person.name like "%{text}%"'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def surchargeLessThan(cur, con):
    maxSurcharge = input("Enter part of name: ")
    try:
        query = f'SELECT name AS showName FROM `show` WHERE `show`.surcharge < {maxSurcharge};'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")


def showsForAd(cur, con):
    serialNo = input("Ad Serial No: ")
    try:
        query = f'SELECT showDate, showStartTime, channelName FROM showGenre WHERE name IN (SELECT name As AdGenrename FROM ad INNER JOIN adGenre on serialNo = adSerialNo WHERE serialNo = {serialNo});'
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
        print("\nError: READ FAILED!\n")
