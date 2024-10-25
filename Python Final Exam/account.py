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