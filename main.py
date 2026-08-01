accounts = {}

def load_accounts():

    accounts.clear()

    with open("accounts.txt","r") as file:

        data = file.readlines()

        for account in data:
            account = account.strip()

            if account:
                acc_num,name,balance = account.split(",")

                accounts[acc_num]={
                    "Name":name,
                    "Balance":float(balance)
                }

def save_accounts():

    with open("accounts.txt","w") as file:

        for account in accounts:

            name = accounts[account]["Name"]
            balance = accounts[account]["Balance"]

            file.write(account + "," + name + "," + str(balance) + "\n")

def acc_num_generator():

    if len(accounts) == 0:
        return "1001"

    acc = 1000

    for account in accounts:

        acc = int(account)

    acc = acc + 1

    return str(acc)
    
def create_accounts():

    print("\n===== Create Account =====")

    name = input("\nEnter Name : ")

    account = acc_num_generator()

    accounts[account]={
        "Name":name,
        "Balance":0
    }
    save_accounts()
    print("\nAccount Created Successfully")
    print("Account Number :", account)
    print("Account Name :", name)
    print("Account Balance : 0" )

def search_accounts():

    print("\n===== Search Account =====")

    acc_num = input("\n Enter Account Number : ")

    if acc_num in accounts:
        print("\nAccount Found")
        print("Name :", accounts[acc_num]["Name"])
        print("Balance :", accounts[acc_num]["Balance"])
        
    else:
        print("\nAccount Not Found")

def deposit():

    print("\n===== Deposit Money =====")

    acc_num = input("\nEnter Account Number : ")

    if acc_num in accounts:

        amount = float(input("\n Enter Amount : "))

        if amount > 0:
            
            accounts[acc_num]["Balance"] = accounts[acc_num]["Balance"] + amount

            save_accounts()

            print("\n Deposit Successfully")

        else:
            print("\n Invalid Amount")

    else:
        print("\nAccount Not Found")


def withdraw():

    print("\n===== Withdraw Amount =====")

    acc_num = input("\nEnter Account Number : ")

    if acc_num in accounts:

        amount = float(input("\nEnter Amount : "))

        if amount <= 0:
            print("\nInvalid Amount")

        elif amount <= accounts[acc_num]["Balance"]:

            accounts[acc_num]["Balance"] = accounts[acc_num]["Balance"] - amount

            save_accounts()

            print("\nWithdraw Successfully")

        else:
            print("\nInsufficient Amount")

    else:
        print("\nAccount Not Found")

def show_all_acc():

    print("\n===== Accounts List =====")

    if len(accounts) == 0:
        print("\nAccount List Empty")
    else:
        print("\n===== All Accounts =====")

        for account in accounts:

            print("\n--------------------")
            print("Account Number :", account)
            print("Account Name :", accounts[account]["Name"])
            print("Account Balance :", accounts[account]["Balance"])

load_accounts()

while True:

    print("\n========== Bank Managment System ==========")
    print("\n1. Create Account")
    print("2. Search Account")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("\nSelect Option : ")

    if choice == "1":
        create_accounts()
    elif choice == "2":
        search_accounts()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        show_all_acc()
    elif choice == "6":
        print("\nExit Successfully")
        break
    else:
        print("\nInvalid Option")

    input ("\n Press Enter To Proceed")