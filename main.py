import sqlite3

# open('db.sqlite','w+')

conn = sqlite3.connect('db.sqlite')

def create_table():


    create_table_sql = """CREATE TABLE Persons (
        PersonID int primary key,
        LastName varchar(255),
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255)
    );"""

    conn.execute(create_table_sql)

def add_person(lastname,firstname,address,city):
    sql = f"""INSERT INTO Persons (Lastname, FirstName, Address, City)
        VALUES ('{lastname}', '{firstname}', '{address}', '{city}');"""
    print(sql)
    conn.execute(sql)
    conn.commit()

# add_person('Rita','Chen','address','New Taipei City')

def update_person(lastname,firstname,address,city,personID):
    sql = f"""UPDATE Persons
             SET LastName = '{lastname}', FirstName = '{firstname}',Address='{address}',City= '{city}'
             WHERE PersonID = '{personID}';"""
    print(sql)
    conn.execute(sql)
    conn.commit()
# update_person('LiLi','Chang','address','Taipei','2')

def delete_person(personID):
    sql = f"""DELETE FROM Persons WHERE PersonID={personID}"""
    print(sql)
    conn.execute(sql)
    conn.commit()
# delete_person('6')

def select_person(personID):
    sql = f"""SELECT LastName,FirstName FROM Persons WHERE PersonID={personID}"""
    print(sql)
    result = conn.execute(sql)
    return result
    # conn.commit()
persons = select_person('9').fetchall()
print(persons)
