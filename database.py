import sqlite3

CreateTable='''Create table IF NOT EXISTS BankDB(AccNo integer primary key, Name Text,
 Mobile integer, Email Text, City Text, Balance Real);'''
InsertTable="Insert INTO BankDB(AccNo,Name, Mobile, Email, City, Balance) values (?, ?, ?, ?, ?, ?);"
GetAllDetailsAccno="SELECT * FROM BankDB Order BY AccNo;"
GetAllDetailsName="SELECT * FROM BankDB ORDER BY Name;"
GetAllDetailsBal="SELECT * FROM BankDB ORDER BY Balance;"
GetDetailsByName="Select * FROM BankDB where Name=?;"
GetDetailsByAccNo="Select * FROM BankDB where AccNo=?;"
UpdateName="Update BankDB set  Name= ? where AccNo = ?;"
UpdateMobile="Update BankDB set  Mobile= ? where AccNo = ?;"
UpdateEmail="Update BankDB set  Email= ? where AccNo = ?;"
UpdateCity="Update BankDB set  City= ? where AccNo = ?;"
UpdateBalance="UPDATE BankDB set Balance = ? where AccNo=?;"
GetBalance="SELECT Balance FROM BankDB where AccNo=?"
DELETE= 'DELETE FROM BankDB WHERE AccNo = ?;'


def connect():
    return sqlite3.connect("data.db")

def createTable(connection):
    with connection:
        connection.execute(CreateTable)

def insertTable(connection,AccNo, Name, Mobile, Email, City, Balance):
    with connection:
        connection.execute(InsertTable, (AccNo, Name, Mobile, Email, City, Balance))

def getAllDetailsAccNo(connection):
    with connection:
        return connection.execute(GetAllDetailsAccno).fetchall()

def getAllDetailsName(connection):
    with connection:
        return connection.execute(GetAllDetailsName).fetchall()

def getAllDetailsBal(connection):
    with connection:
        return connection.execute(GetAllDetailsBal).fetchall()

def getDetailsByName(connection, Name): 
    with connection:
        return connection.execute(GetDetailsByName,(Name,)).fetchall()

def getDetailsByAccNo(connection, AccNo): 
    with connection:
        return connection.execute(GetDetailsByAccNo,(AccNo,)).fetchall()

def updateName(connection,Name,AccNo):
    with connection:
        connection.execute(UpdateName,(Name,AccNo,))

def updateMobile(connection,Mobile,AccNo):
    with connection:
        connection.execute(UpdateMobile,(Mobile,AccNo,))

def updateEmail(connection,Email,AccNo):
    with connection:
        connection.execute(UpdateEmail,(Email,AccNo,))

def updateCity(connection,City,AccNo):
    with connection:
        connection.execute(UpdateCity,(City,AccNo,))
    
def updateBalance(connection,Balance,AccNo):
    with connection:
        connection.execute(UpdateBalance,(Balance,AccNo,))

def deleteAcc(connection,AccNo):
    with connection:
        connection.execute(DELETE,(AccNo,))