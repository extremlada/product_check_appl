import mysql.connector


def connection_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="items_barcode"
    )
    return mydb


def commit_mysql(mydb, *args):
    if len([*args] ) > 9:
        raise ValueError("Exactly 9 arguments required")

    mycursor = mydb.cursor()
    # ez egy formula a %s place holderek
    sqlFormula = ("INSERT INTO barcode_name (categoryName, brandName, productName, eancode, packageSize, netPrice, grossPrice, netDiscountedPrice, isDiscounted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    #igy használjuk a formulat

    mycursor.execute(sqlFormula, args)

    #ezzel tudjuk menteni a changeket!!!!!!!!
    mydb.commit()


def read_mysql(mydb, barcode):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM `barcode_name` WHERE `eancode` = %s", (barcode,))
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)

def eancode_exists(mydb, eancode):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM barcode_name WHERE eancode = %s"
    val = (eancode,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result is not None