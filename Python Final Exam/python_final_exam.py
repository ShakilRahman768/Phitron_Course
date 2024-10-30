from datetime import datetime
import random

class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(1000, 9999)
        self.transaction_history = []
        self.loan_count = 0

class AdminAccount:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.admin_id = random.randint(9000, 9999)

class Bank:
    def __init__(self):
        self.accounts = {}
        self.admin_accounts = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature_enabled = True
        self.is_bankrupt = False
    
    def create_admin_account(self, name, email, password):
        while True:
            admin = AdminAccount(name, email, password)
            if admin.admin_id not in self.admin_accounts:
                self.admin_accounts[admin.admin_id] = admin
                return admin.admin_id

    def verify_admin(self, admin_id, password):
        if admin_id in self.admin_accounts:
            return self.admin_accounts[admin_id].password == password
        return False

    def create_account(self, name, email, address, account_type):
        while True:
            account = Account(name, email, address, account_type)
            if account.account_number not in self.accounts:
                self.accounts[account.account_number] = account
                return account.account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            self.total_balance -= self.accounts[account_number].balance
            del self.accounts[account_number]
            return True
        return False

    def get_account_list(self):
        return [(acc.account_number, acc.name, acc.balance) for acc in self.accounts.values()]

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account.balance += amount
            self.total_balance += amount
            account.transaction_history.append(
                (datetime.now(), "Deposit", amount)
            )
            return True
        return False

    def withdraw(self, account_number, amount):
        if self.is_bankrupt:
            return "Bank is bankrupt. Cannot process withdrawal."
        
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.balance >= amount:
                account.balance -= amount
                self.total_balance -= amount
                account.transaction_history.append(
                    (datetime.now(), "Withdrawal", -amount)
                )
                return True
            return "Withdrawal amount exceeded"
        return "Account not found"

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        return None

    def get_transaction_history(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].transaction_history
        return None

    def take_loan(self, account_number, amount):
        if not self.loan_feature_enabled:
            return "Loan feature is currently disabled"
        
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.loan_count < 2:
                account.balance += amount
                self.total_balance += amount
                self.total_loan += amount
                account.loan_count += 1
                account.transaction_history.append(
                    (datetime.now(), "Loan", amount)
                )
                return True
            return "Maximum loan limit reached"
        return "Account not found"

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            sender = self.accounts[from_account]
            receiver = self.accounts[to_account]
            
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                sender.transaction_history.append(
                    (datetime.now(), f"Transfer to {to_account}", -amount)
                )
                receiver.transaction_history.append(
                    (datetime.now(), f"Transfer from {from_account}", amount)
                )
                return True
            return "Insufficient balance"
        return "Account does not exist"


bank = Bank()
while True:
    print("\n=== Banking System ===")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Create Admin Account")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        while True:
            print("\n=== User Menu ===")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Take Loan")
            print("7. Transfer Money")
            print("8. Back to Main Menu")
            
            user_choice = input("Enter your choice: ")
            
            if user_choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                while True:
                    account_type = input("Enter account type (Savings/Current): ").capitalize()
                    if account_type in ['Savings', 'Current']:
                        break
                    print("Invalid account type! Please enter either 'Savings' or 'Current'")
                
                acc_num = bank.create_account(name, email, address, account_type)
                print(f"Account created successfully! Your account number is: {acc_num}")
            
            elif user_choice == "2":
                try:
                    acc_num = int(input("Enter account number: "))
                    amount = float(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    if bank.deposit(acc_num, amount):
                        print("Deposit successful!")
                    else:
                        print("Account not found!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "3":
                try:
                    acc_num = int(input("Enter account number: "))
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    result = bank.withdraw(acc_num, amount)
                    print(result if isinstance(result, str) else "Withdrawal successful!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "4":
                try:
                    acc_num = int(input("Enter account number: "))
                    balance = bank.check_balance(acc_num)
                    if balance is not None:
                        print(f"Current balance: {balance}")
                    else:
                        print("Account not found!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "5":
                try:
                    acc_num = int(input("Enter account number: "))
                    history = bank.get_transaction_history(acc_num)
                    if history:
                        if len(history) == 0:
                            print("No transactions yet!")
                        else:
                            for date, transaction_type, amount in history:
                                print(f"{date}: {transaction_type} - {amount}")
                    else:
                        print("Account not found!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "6":
                try:
                    acc_num = int(input("Enter account number: "))
                    amount = float(input("Enter loan amount: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    result = bank.take_loan(acc_num, amount)
                    print(result if isinstance(result, str) else "Loan approved!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "7":
                try:
                    from_acc = int(input("Enter your account number: "))
                    to_acc = int(input("Enter recipient account number: "))
                    amount = float(input("Enter amount to transfer: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    result = bank.transfer(from_acc, to_acc, amount)
                    print(result if isinstance(result, str) else "Transfer successful!")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            
            elif user_choice == "8":
                break
            
            else:
                print("Invalid choice! Please try again.")
    
    elif choice == "2":
        try:
            admin_id = int(input("Enter admin ID: "))
            password = input("Enter admin password: ")
            
            if bank.verify_admin(admin_id, password):
                while True:
                    print("\n=== Admin Menu ===")
                    print("1. Delete User Account")
                    print("2. Show All Accounts")
                    print("3. Check Total Balance")
                    print("4. Check Total Loan")
                    print("5. On/Off Loan Feature")
                    print("6. Back to Main Menu")
                    
                    admin_choice = input("Enter your choice: ")
                    
                    if admin_choice == "1":
                        try:
                            acc_num = int(input("Enter account number to delete: "))
                            if bank.delete_account(acc_num):
                                print("Account deleted successfully!")
                            else:
                                print("Account not found!")
                        except ValueError:
                            print("Invalid input! Please enter numbers only.")
                    
                    elif admin_choice == "2":
                        accounts = bank.get_account_list()
                        if len(accounts) == 0:
                            print("No accounts exist in the bank!")
                        else:
                            print("\nAccount List:")
                            print("Account Number | Name | Balance")
                            print("-" * 40)
                            for acc_num, name, balance in accounts:
                                print(f"{acc_num:13} | {name:15} | {balance:7}")
                    
                    elif admin_choice == "3":
                        print(f"Total bank balance: {bank.total_balance}")
                    
                    elif admin_choice == "4":
                        print(f"Total loan amount: {bank.total_loan}")
                    
                    elif admin_choice == "5":
                        bank.loan_feature_enabled = not bank.loan_feature_enabled
                        status = "enabled" if bank.loan_feature_enabled else "disabled"
                        print(f"Loan feature is now {status}")
                    
                    elif admin_choice == "6":
                        break
                    
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Invalid admin ID or password!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
    elif choice == "3":
        print("\n=== Create Admin Account ===")
        name = input("Enter admin name: ")
        email = input("Enter admin email: ")
        password = input("Create admin password: ")
        
        admin_id = bank.create_admin_account(name, email, password)
        print(f"\nAdmin account created successfully!")
        print(f"Your Admin ID is: {admin_id}")
        print("Please save this ID and your password for future login.")
    
    elif choice == "4":
        print("Thank you for using our banking system!")
        break
    
    else:
        print("Invalid choice! Please try again.")
