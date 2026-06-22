class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        # 1. Create two private variables
        self.__account_number = account_number
        self.__balance = initial_balance

    # 2. Create private methods
    def __validate_amount(self, amount):
        """Checks whether the amount is greater than 0."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        return True

    def __show_account_type(self):
        """Displays the account type."""
        return "Savings Account"

    # 3. Create getter methods
    def get_account_number(self):
        """Retrieve the account number."""
        if not self.__account_number:
            raise ValueError("Account number is uninitialized or invalid.")
        return self.__account_number

    def get_balance(self):
        """Retrieve the current balance."""
        if self.__balance is None or self.__balance < 0:
            raise ValueError("Account balance data is corrupted.")
        return self.__balance

    # 4. Create a setter method
    def deposit(self, amount_input):
        """Deposit money into the account and update balance."""
        try:
            amount = float(amount_input)
        except ValueError:
            raise TypeError("Invalid input type. Please enter a valid number.")

        self.__validate_amount(amount)
        self.__balance += amount


# 5. Main Execution Flow
def main():
    print("--- Bank Account Management System ---\n")
    
    # Take ALL data as user input
    user_account_number = input("Enter your Account Number to create an account: ")
    
    # Handle the initial balance input safely
    try:
        user_initial_balance = float(input("Enter your initial balance: "))
    except ValueError:
        print("Invalid initial balance entered. Defaulting to $0.0")
        user_initial_balance = 0.0

    # Create the object using the user's input
    account = BankAccount(account_number=user_account_number, initial_balance=user_initial_balance)

    # Open (or create) the bank.txt file to store the details
    # Using "a" mode so it appends new sessions without deleting old ones
    with open("bank.txt", "a") as file:
        file.write("\n--- New Transaction Log ---\n")
        
        try:
            # Get and display the account number
            acc_num = account.get_account_number()
            print(f"\nAccount Number: {acc_num}")
            file.write(f"Account Number: {acc_num}\n")
            
            # Get and display the current balance
            curr_bal = account.get_balance()
            print(f"Starting Balance: RS.{curr_bal:.2f}")
            file.write(f"Starting Balance: RS.{curr_bal:.2f}\n")
            
            # Take deposit amount as user input
            deposit_input = input("\nEnter amount to deposit: ")
            
            # Deposit the amount
            account.deposit(deposit_input)
            print("Deposit successful!")
            file.write(f"Deposit Made: RS.{float(deposit_input):.2f}\n")
            
            # Get and display the updated balance
            updated_bal = account.get_balance()
            print(f"\nUpdated Balance: RS.{updated_bal:.2f}")
            file.write(f"Updated Balance: RS.{updated_bal:.2f}\n")
            
            print("\n✔️ All transaction details have been successfully saved to 'bank.txt'.")
            file.write("Status: Transaction Successful\n")

        # Catch exceptions and log the errors to the file as well
        except ValueError as e:
            error_msg = f"Value Error: {e}"
            print(f"\n{error_msg}")
            file.write(f"Status: Failed - {error_msg}\n")
        except TypeError as e:
            error_msg = f"Type Error: {e}"
            print(f"\n{error_msg}")
            file.write(f"Status: Failed - {error_msg}\n")
        except Exception as e:
            error_msg = f"An unexpected error occurred: {e}"
            print(f"\n{error_msg}")
            file.write(f"Status: Failed - {error_msg}\n")

if __name__ == "__main__":
    main()