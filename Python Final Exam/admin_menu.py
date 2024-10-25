def admin_menu(bank):
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
                print("5. Toggle Loan Feature")
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