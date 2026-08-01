# Dictionary used to store all accounts
accounts = {}

# Load all account records from accounts.txt
def load_accounts():

    # Remove old data before loading fresh data
    accounts.clear()

    # Open file in read mode
    with open("accounts.txt","r") as file:

        # Read all lines from file
        data = file.readlines()

        # Loop through every line
        for account in data:

            # Remove extra spaces and newline characters
            account = account.strip()

            # Ignore empty lines
            if account:

                # Split account number, name and balance
                acc_num,name,balance = account.split(",")

                # Store account inside dictionary
                accounts[acc_num]={
                    "Name":name,
                    "Balance":float(balance)
                }

# Save updated account information into accounts.txt
def save_accounts():

    # Open file in write mode
    with open("accounts.txt","w") as file:

        # Loop through every account
        for account in accounts:

            name = accounts[account]["Name"]
            balance = accounts[account]["Balance"]

            # Write account data into file
            file.write(account + "," + name + "," + str(balance) + "\n")

# Generate a new account number automatically
def acc_num_generator():

    # If no account exists, start from 1001
    if len(accounts) == 0:
        return "1001"

    acc = 1000

    # Find the last account number
    for account in accounts:
        acc = int(account)

    # Generate next account number
    acc = acc + 1

    return str(acc)


# Create a new bank account
def create_accounts():

    print("\n===== Create Account =====")

    # Get account holder name
    name = input("\nEnter Name : ")

    # Generate unique account number
    account = acc_num_generator()

    # Create account with zero balance
    accounts[account]={
        "Name":name,
        "Balance":0
    }

    # Save account into file
    save_accounts()

    print("\nAccount Created Successfully")
    print("Account Number :", account)
    print("Account Name :", name)
    print("Account Balance : 0")


# Search an account using account number
def search_accounts():

    print("\n===== Search Account =====")

    acc_num = input("\n Enter Account Number : ")

    if acc_num in accounts:

        print("\nAccount Found")
        print("Name :", accounts[acc_num]["Name"])
        print("Balance :", accounts[acc_num]["Balance"])

    else:
        print("\nAccount Not Found")

# Deposit money into an account
def deposit():

    print("\n===== Deposit Money =====")

    acc_num = input("\nEnter Account Number : ")

    if acc_num in accounts:

        amount = float(input("\n Enter Amount : "))

        # Accept only positive amount
        if amount > 0:

            # Update balance
            accounts[acc_num]["Balance"] += amount

            # Save updated data
            save_accounts()

            print("\nDeposit Successfully")

        else:
            print("\nInvalid Amount")

    else:
        print("\nAccount Not Found")


# Withdraw money from an account
def withdraw():

    print("\n===== Withdraw Amount =====")

    acc_num = input("\nEnter Account Number : ")

    if acc_num in accounts:

        amount = float(input("\nEnter Amount : "))

        # Reject zero or negative amount
        if amount <= 0:
            print("\nInvalid Amount")

        # Check available balance
        elif amount <= accounts[acc_num]["Balance"]:

            # Deduct amount
            accounts[acc_num]["Balance"] -= amount

            # Save updated data
            save_accounts()

            print("\nWithdraw Successfully")

        else:
            print("\nInsufficient Amount")

    else:
        print("\nAccount Not Found")


# Display all bank accounts
def show_all_acc():

    print("\n===== Accounts List =====")

    # Check if account list is empty
    if len(accounts) == 0:

        print("\nAccount List Empty")

    else:

        print("\n===== All Accounts =====")

        # Display every account
        for account in accounts:

            print("\n--------------------")
            print("Account Number :", account)
            print("Account Name :", accounts[account]["Name"])
            print("Account Balance :", accounts[account]["Balance"])


# Load existing accounts before program starts
load_accounts()

# Main program loop
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