from account import Bank
from user_menu import user_menu
from admin_menu import admin_menu


bank = Bank()
    
while True:
    print("\n=== Banking System ===")
    print("1. User Menu")
    print("2. Admin Menu")
    print("3. Create Admin Account")
    print("4. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        user_menu(bank)
        
    elif choice == "2":
        admin_menu(bank)
        
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