def user_menu(bank):
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