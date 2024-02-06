#Create your own real-life example problems related to your hobbies, interests, or daily routines. Think 
#creatively and apply your understanding of variables, operators, and expressions to solve at least 3 
#practical problems.

#monthly budget Calculator\
budget=30000
while True:
 
    groceries=int(input("Enter groceries amount: "))
    house_Rent=int(input("Enter your house rent: "))
    traveling_expense=int(input("Enter your traveling expense: "))
    internet_Bill=int(input("enter your internet Bill:  "))
    phone_bill=int(input("Enter your phone bill: "))
    gym=int(input("enter your gym fee: "))
    total_expense=(groceries+house_Rent+traveling_expense+internet_Bill+phone_bill+gym)
    print(f"YOUR TOTAL EXPENSE IS {total_expense} PKR")
    if total_expense>budget:
        print("You are crossing you budget")
    else:
        print("You are in under budget keep maneging your budget like this")
        user_input = input("Do You Want To Continue (YES/NO): ")
        if user_input.upper() != "YES":
            break