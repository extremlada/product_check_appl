import mysql.connector


def connection_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )
    return mydb


def commit_mysql(mydb, *args):
    if len([*args] ) > 6:
        raise ValueError("Exactly 6 arguments required")

    mycursor = mydb.cursor()
    # ez egy formula a %s place holderek
    sqlFormula = "INSERT INTO barcode_name (Barcode, title, category, metadata, metanutritions, brand, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    #igy használjuk a formulat

    mycursor.execute(sqlFormula, args)

    #ezzel tudjuk menteni a changeket!!!!!!!!
    mydb.commit()


connection_mysql()
