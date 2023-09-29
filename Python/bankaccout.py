class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Initialize a bank account with an account holder's name and an optional initial balance
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Deposit funds into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Withdraw funds from the account
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        # Get the current account balance
        return self.balance

    def __str__(self):
        # String representation of the account
        return f"Account Holder: {self.account_holder}\nBalance: ${self.balance}"


def main():
    print("Welcome to the Bank Account Management System")

    # Create a new bank account
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: $"))
    account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current Balance: ${account.get_balance()}")
        elif choice == "4":
            print("Thank you for using the Bank Account Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

# <Bankaccounts> by Moutasim Qazi