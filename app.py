import database
import func
import charts
import matplotlib.pyplot as plt
MENU_PROMPT='''
---Bank Management System---

Please choose one of these options :-

1)Insert New Record.
2)See all Records by-
3)Find Records by-
4)Udate Records.
5)Credit. 
6)Debit.
7)Delete Account.
8)EXIT.

Your Selection :-
'''
OrderBy='''
    a)Ordered by Account Number.
    b)Ordered by Name.
    c)Ordered by Balance.
Your Selection :-
'''
UPDATE='''
    a)Name
    b)Mobile number
    c)Email
    d)City
Your Selection :-
'''
FindBy='''
    a) Account Number.
    b) Name.
'''

def menu():
    connection=database.connect()
    database.createTable(connection)

    while (user_input := input(MENU_PROMPT)) != '8':
        if user_input=="1":
            func.userInput(connection)
                             
        elif user_input=="2":
            orderInput=input(OrderBy)
            func.OrderInput(connection,orderInput)            
            
        elif user_input=="3":
            FindByInput=input(FindBy)
            func.findByInput(connection,FindByInput)
        
        elif user_input=='4':
            updateInput=input(UPDATE)
            func.update(connection,updateInput)

        elif user_input=='5':
            func.credit(connection)
            
        elif user_input=='6':
            func.debit(connection)

        elif user_input=='7':
            func.delete(connection) 

        else:
            print("Invalid input please enter again")


        """elif user_input=='5':
            methods_to_rating=database.get_method_to_rating(connection)
            charts.method_to_rating_bar(methods_to_rating)
            plt.show()"""


menu()  