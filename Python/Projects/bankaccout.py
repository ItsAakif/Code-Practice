import random
import datetime

class BankAccount:
    def __init__(self, account_holder, account_type, initial_balance=0):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = initial_balance
        self.account_number = self.generate_account_number()
        self.transactions = []

    def generate_account_number(self):
        return ''.join(random.choice('0123456789') for _ in range(10))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount} at {datetime.datetime.now()}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount} at {datetime.datetime.now()}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return f"Account balance for {self.account_holder}: ${self.balance}"

    def get_account_history(self):
        return "\n".join(self.transactions)

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Type: {self.account_type}\nAccount Number: {self.account_number}\nBalance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, account_type, initial_balance=0):
        account = BankAccount(account_holder, account_type, initial_balance)
        self.accounts[account.account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return f"Account {account_number} closed successfully."
        else:
            return "Account not found."

def main():
    bank = Bank()

    while True:
        print("\nBank Account Management Menu:")
        print("1. Create an Account")
        print("2. Access an Account")
        print("3. Close an Account")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            account_holder = input("Enter the account holder's name: ")
            account_type = input("Enter the account type (Savings/Checking): ").capitalize()
            initial_balance = float(input("Enter the initial balance: "))
            account = bank.create_account(account_holder, account_type, initial_balance)
            print(f"Account created successfully:\n{account}")
        elif choice == '2':
            account_number = input("Enter the account number: ")
            account = bank.get_account(account_number)
            if account:
                while True:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. View Account History")
                    print("5. Back to Main Menu")
                    sub_choice = input("Enter your choice (1/2/3/4/5): ")

                    if sub_choice == '1':
                        amount = float(input("Enter the deposit amount: "))
                        print(account.deposit(amount))
                    elif sub_choice == '2':
                        amount = float(input("Enter the withdrawal amount: "))
                        print(account.withdraw(amount))
                    elif sub_choice == '3':
                        print(account.get_balance())
                    elif sub_choice == '4':
                        print(account.get_account_history())
                    elif sub_choice == '5':
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = input("Enter the account number to close: ")
            result = bank.close_account(account_number)
            print(result)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
# <Bankaccount> by Moutasim Qazi
