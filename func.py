import database

def userInput(connection):
    AccNo=int(input("Enter Account Number to be inserted: "))
    Name=input("Enter the name of the Account Holder: ")
    Mobile=int(input("Enter the mobile number of the account holder: "))
    Email=input("Enter the email address of the account holder: ")
    City=input("Enter the City of the account holder: ")
    Balance=int(input("Enter the balance in the account: "))
    database.insertTable(connection, AccNo, Name, Mobile, Email, City, Balance)       

def OrderInput(connection,orderInput):
    
    if orderInput=='a':
        data = database.getAllDetailsAccNo(connection)
        for d in data:
            print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]}") 
    
    elif orderInput=='b':
        data = database.getAllDetailsName(connection)
        for d in data:
            print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]}") 
    
    elif orderInput=='c':
        data = database.getAllDetailsBal(connection)
        for d in data:
            print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]}") 
    
    else:
        print("Invalid Input")
        
def update(connection,updateInput):
    if updateInput=='a':
        Name=input("Enter new name: ")
        AccNo=int(input("Enter Account number of the holder: "))
        database.updateName(connection, Name, AccNo)

    elif updateInput=='b':
        Mobile=int(input("Enter new mobile number: "))
        AccNo=int(input("Enter Account number of the holder: "))
        database.updateMobile(connection, Mobile, AccNo)
    
    elif updateInput=='c':
        Email=input("Enter new Email address: ")
        AccNo=int(input("Enter Account number of the holder: "))
        database.updateEmail(connection, Email, AccNo)

    elif updateInput=='d':
        City=input("Enter new City: ")
        AccNo=int(input("Enter Account number of the holder: "))
        database.updateCity(connection, City, AccNo)
    
    else:
        print("Invalid Input.")

def findByInput(connection,FindByInput):
    if FindByInput=='b':
        Name=input("Enter the Name of the account holder whose account detail you want to find: ")
        data=database.getDetailsByName(connection, Name)
        for d in data:
            print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]}")

    elif FindByInput=='a':
        AccNo = input("Enter the Account Number whose account detail you want to find: ")
        data=database.getDetailsByAccNo(connection, AccNo)
        for d in data:
            print(f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]}")
    
    else:
        print("Invalid Input")

def credit(connection):
    AccNo=int(input("Enter account number you want to credit into: "))
    bal=int(input("Enter amount you want to credit in: "))
    with connection:
            tupbal=connection.execute(database.GetBalance,(AccNo,)).fetchone()
            Balance=int(tupbal[0])
            Balance=Balance + bal
            connection.execute(database.UpdateBalance,(Balance,AccNo,))

def debit(connection):
    AccNo=int(input("Enter account number you want to debit from: "))
    bal=int(input("Enter amount you want to withdraw: "))
    with connection:
            tupbal=connection.execute(database.GetBalance,(AccNo,)).fetchone()
            Balance=int(tupbal[0])
            if Balance > bal:
                Balance=Balance - bal
                connection.execute(database.UpdateBalance,(Balance,AccNo,))
            else:
                print("    There is not enough balance")

def delete(connection):
    AccNo=int(input("Enter Account Number you want to delete: "))
    ans=input("Are you sure? (y/n): ")
    if ans=='y':
        database.deleteAcc(connection,AccNo)
        print(f"Account Number - {AccNo} is deleted permanently.")
    else:
        print(f"Account Number - {AccNo} is  not deleted.")