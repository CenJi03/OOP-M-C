import os
import datetime
from login_system import authenticate_user, log_login_success
from library_system import manageLibrary


def display_header():
    """Display a welcome header for the application"""
    print("\n" +
          "=" * 125 +
          "\n          WELCOME TO LIBRARY MANAGEMENT SYSTEM\n" +
          "=" * 125 + "\n")


def display_login_dashboard():
    """Display the login dashboard options"""
    print("\n" +
          "=" * 60 + " LOGIN DASHBOARD " + "=" * 60)
    print("    1. LOGIN       2. LOGOUT       3. EXIT")
    print("=" * 125)


def get_dashboard_input():
    """Get user input for dashboard options with validation"""
    while True:
        choice = input("---> Choose Your Option: ").strip()
        if choice in {'1', '2', '3'}:
            return int(choice)
        print("---> Invalid option. Please enter 1, 2, or 3.")


def main():
    """Main function that runs the application"""
    # Ensure required directories exist
    os.makedirs('UserInfo', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Create sample user accounts file if it doesn't exist
    if not os.path.exists('UserInfo/UserAccounts.csv'):
        print("Creating sample user accounts file...")
        with open('UserInfo/UserAccounts.csv', 'w', newline='') as f:
            f.write("admin,admin\n")
    
    display_header()
    
    # Set specific date/time for display
    specific_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    logged_in = False
    username = None
    
    while True:
        display_login_dashboard()
        choice = get_dashboard_input()
        
        if choice == 1:  # Login
            if logged_in:
                print("\n---> Returning to library management system...\n")
                print("-" * 60)
                exit_code = manageLibrary(username, specific_time)
                if exit_code is not True:
                    print("\n---> Unexpected return from library system.")
            else:
                auth_successful, current_user = authenticate_user()
                if auth_successful:
                    logged_in = True
                    username = current_user
                    print("-" * 60)
                    input("\nPress Enter to continue to the Library Management System...\n")
                    exit_code = manageLibrary(username, specific_time)
                    if exit_code is not True:
                        print("\n---> Unexpected return from library system.")
                else:
                    print("\n---> Login failed. Please try again.")
                    input("\nPress Enter to continue...\n")
        
        elif choice == 2:  # Logout
            if logged_in:
                print(f"---> Goodbye, {username}! You have been logged out.")
                logged_in = False
                username = None
            else:
                print("\n---> You are not currently logged in.")
            input("\nPress Enter to continue...\n")
        
        elif choice == 3:  # Exit
            print("---> Thank you for using the Library Management System. Goodbye!\n")
            break


if __name__ == "__main__":
    main()