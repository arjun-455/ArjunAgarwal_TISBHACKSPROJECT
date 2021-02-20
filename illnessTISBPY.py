import sqlite3
passw = "doctor"
try:
   sqlite_Connection = sqlite3.connect('illnessTISB')
   conn = sqlite_Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)



def printrow(x):
    for row in x:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Ingridient 1  = ", row[2])
            print("Ingredient 2  = ", row[3])
            print("Ingredient 3  = ",row [4], "\n\n")



conn = sqlite3.connect('illnessTISB')
cursor = conn.cursor()


while (True):
    print("\n\n\n\t\t\t","EVERYDAY ILLNESSES")
    print("\t\t","1. FIND AN ILLNESS")
    print("\t\t","2. ADD ILLNESS")
    print("\t\t","3. EDIT A PRE-EXISTING ILLNESS")
    print("\t\t","4. SHOW ALL ILLNESSES")
    print("\t\t","5. Search for recipies with specific Ingredients")
    print("\t\t", "6. EXIT PROGRAM")

    opt = int(input("ENTER YOUR OPTIONS: "))

    if opt == 1:
        d = str(input("ENTER THE ILLNESS NAME: "))
        di = d.upper()
        sql_stat= """SELECT * FROM illness WHERE NAME = ?"""
        cursor.execute(sql_stat,(di,))

        records = cursor.fetchall()

        printrow(records)
    if opt == 2:
        try1 = input("PLEASE ENTER THE PASSWORD TO EDIT THIS: ")
        try2 = try1.upper()
        if try2 == passw:
            n = input("ENTER THE NAME OF THE ILLNESS: ")
            i1 = input("ENTER THE FIRST SYMPTOM: ")
            i2 = input("ENTER THE SECOND SYMPTOM: ")
            i3 = input("ENTER THE THIRD SYMPTOM: ")
            n = n.upper()
            i1 = i1.upper()
            i2 = i2.upper()
            i3 = i3.upper()
        
            cursor.execute("INSERT INTO illness (NAME,symptom_1, symptom_2, symptom_3) VALUES (?,?,?,?)",(n,i1,i2,i3))
            conn.commit()
            print("ILLNESS ADDED SUCCESSFULLY")
        else:
                print("UNAUTHORISED PERSONNEL MAY NOT ACCESS THIS FEATURE")
    if opt == 3:
        try1 = input("PLEASE ENTER THE PASSWORD TO EDIT THIS: ")
        try2 = try1.upper()
        if try1 == passw:
            d = str(input("ENTER THE ILLNESS NAME WHICH IS TO BE UPDATED: "))
            di = d.upper()
            i1 = input("ENTER THE NEW SYMPTOM 1: ")
            i2 = input("ENTER THE NEW SYMPTOM 2: ")
            i3 = input("ENTER THE NEW SYMPTOM 3: ")
            i1 = i1.upper()
            i2 = i2.upper()
            i3 = i3.upper()

            sql_stat = """ Update illness set symptom_1 = ?, symptom_2 = ?, symptom_3 = ?  WHERE NAME = ?"""
            cursor.execute(sql_stat,(i1,i2,i3,di,))
            conn.commit()
            print("\nDatabase has been updated")
        else:
            print("UNAUTHORISED PERSONNEL MAY NOT ACCESS THIS FEATURE")
    if opt == 4:
        sql_select_Query = "SELECT * from illness"
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Printing each Recipie\n\n")
        printrow(records)

    if opt == 5:
        cho = int(input("Enter the number of search parameters: "))
        if cho == 1:
            i = input("Enter the symptom you wish to search for: ")
            i = i.upper()
            sql_stat = "SELECT * from illness WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i,i,i,))
            i1 = cursor.fetchall()
            printrow(i1)
        if cho == 2:
            i = input("Enter the first illness you wish to search for: ")
            i = i.upper()
            sql_stat = "SELECT * from illness WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i,i,i,))
            x = cursor.fetchall()
            for row in x:
                lrow = list(row)         
                sql_stat1 = "INSERT INTO search (ID,NAME, symptom_1, symptom_2, symptom_3) VALUES (?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4])

                del lrow[0:4]
                conn.commit()
            
            i2 = input("Enter the second symptom you wish to search for: ")
            i2 = i.upper()
            sql_stat = "SELECT * from search WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i2,i2,i2,))
            y = cursor.fetchall()
            printrow(y)
            cursor.execute("DELETE FROM search")

        if cho == 3:
            i = input("Enter the first symptom you wish to search for: ")
            i = i.upper()
            sql_stat = "SELECT * from illness WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i,i,i,))
            x = cursor.fetchall()
            printrow(x)
            for row in x:
                rrow = list(row)         
                sql_stat1 = "INSERT INTO search (ID,NAME, symptom_1, symptom_2, symptom_3) VALUES (?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4])

                del rrow[0:4]
                conn.commit()
            
            i2 = input("Enter the second symptom you wish to search for: ")
            i2 = i.upper()
            sql_stat = "SELECT * from search WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i2,i2,i2,))
            y = cursor.fetchall()
            printrow(y)
            cursor.execute("DELETE FROM search")

            for row in y:
                lrow = list(row)
                sql_stat1 = "INSERT INTO search (ID,NAME, symptom_1, symptom_2, symptom_3) VALUES (?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4])

                conn.commit()
                del lrow[0:4]
            

            i3 = input("Enter the third symptom you wish to search for: ")
            i3 = i.upper()
            sql_stat = "SELECT * from search WHERE symptom_1 = ? OR symptom_2 = ? OR symptom_3 = ?"
            cursor.execute(sql_stat, (i3,i3,i3,))
            a = cursor.fetchall()
            printrow(a)
            cursor.execute("DELETE FROM search")
    if opt == 6:
        break


        
