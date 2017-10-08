import sqlite3

conn = sqlite3.connect("MyDb.db");

cursor = conn.cursor();
try:
    cursor.execute("Create TABLE if not exists MYTABLE (_ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL)");
except Exception as e:
    print(str(e))
else:
    print("Created Successfully")


def insertData(data):
    try:
        cursor.execute("INSERT INTO MYTABLE (NAME) VALUES ('" + data + "')")
        conn.commit()
        print('Inserted')
    except Exception as e:
        conn.rollback()
        print(str(e))


def read():
    try:
        cursor.execute('SELECT * FROM MYTABLE')
        result = cursor.fetchall()
        print("\n_____________________\n")
        for row in result:
            id = row[0]
            name = row[1]
            print(str(id)+" "+str(name))
        print("\n_____________________")
    except Exception as e:
        conn.rollback()
        print(str(e))


def update(name, key):
    try:
        cursor.execute("UPDATE MYTABLE SET NAME = '" + name + "' WHERE _ID = " + str(key) + "")
        conn.commit()
        print('Updated')
    except Exception as e:
        print(str(e))
        conn.rollback()


def delete(key):
    try:
        cursor.execute("DELETE FROM MYTABLE WHERE _ID = " + str(key) + "")
        conn.commit()
        print('Deleted')
    except Exception as e:
        print(str(e))



while True:
    choice = input("1.add name\n2.read\n3.update\n4.delete\n5.terminate\n")
    if choice == '1':
        data = input("Type Some Thing: ");
        if data != 'no':
            insertData(data)
    elif choice == '2':
        read()
    elif choice == '3':
        new_name = input("Enter new name: ")
        key = int(input("Enter key: "))
        update(new_name, key)
    elif choice == '4':
        key = int(input("Enter key for delete record: "))
        delete(key)
    else:
        break
