menu = (""" Choice an operation!
             
             [1] - Deposit

             [2] - Withdraw 

             [3] - Statement

             [0] - Sign Out
=> """)

account_balance = 0
limit = 500
account_statement = ""
amount_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:

    choice = input(menu)

    if choice == "1":
        value = float(input('How much would you like to deposit?  '))

        if value > 0:
            account_balance += value
            account_statement += f"Deposit: R$ {value:.2f}\n"

        else:
            print("Operation failed! The entered value is invalid.")

    elif choice == "2":
        value = float(input("How much would you like to withdraw? "))

        exceeded_balance = value > account_balance

        exceeded_limit = value > limit

        exceeded_withdraw = amount_withdrawals >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operation failed! You don't have enough balance.")

        elif exceeded_limit:
            print("Operation failed! Withdrawal amount exceeds limit.")

        elif exceeded_withdraw:
            print("Operation failed! Maximum number of withdrawals exceeded.")

        elif value > 0:
            account_balance -= value
            account_statement += f"Withdraw: R$ : {value:.2f}\n"
            amount_withdrawals += 1

        else:
            print("Operation failed! The entered value is invalid.")
    
    elif choice == "3":
        print("\n =========== Account Statement ===========")
        print("There were no transactions in the account." if not account_statement else account_statement)
        print(f"\nBalance: R$ {account_balance:.2f}")
        print("===========================================\n")
    
    elif choice == "0":
        break
    
    else:
        print("Invalid operation, please reselect a new operation.")

