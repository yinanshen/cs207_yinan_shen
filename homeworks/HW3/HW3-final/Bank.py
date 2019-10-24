from enum import Enum
import sys

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount:

    def __init__(self, owner, accountType, balance):
        self.owner = owner
        self.accountType = accountType
        self.balance = balance

    def withdraw(self, amount):
        if (amount < 0):
            raise Exception('You should not be able to withdraw a negative amount.')
        elif (amount > self.balance):
            raise Exception('You should not be able to withdraw more money than the balance of the account.')
        else:
            self.balance -= amount

    def deposit(self, amount):
        if (amount < 0):
            raise Exception('You should not be able to deposit a negative amount.')
        else:
            self.balance += amount

    def __str__(self):
        return '{} owns {}.'.format(self.owner, self.accountType)

    def __len__(self):
        return self.balance


class BankUser:
    def __init__(self, owner):
        self.owner = owner

    def checkAccount(self, accountType):
        if hasattr(self, 'account_dictionary'):
            for key, value in self.account_dictionary.items():
                if key == accountType:
                    return 'account already exists'
                else:
                    return 'different account type found'
        else:
            return 'no account found'

    def addAccount(self, accountType):
        new_account = BankAccount(self.owner, accountType, 0)
        check_result = self.checkAccount(accountType)
        if check_result == 'account already exists':
            raise Exception('The account has already existed.')
        elif check_result == 'different account type found':
            self.account_dictionary[accountType] = new_account
        elif check_result == 'no account found':
            self.account_dictionary = {accountType : new_account}


    def getBalance(self, accountType):
        check_result = self.checkAccount(accountType)
        if check_result == 'account already exists':
            print('The balance is ', self.account_dictionary[accountType].balance)
            return self.account_dictionary[accountType].balance
        else:
            raise Exception('The account does not exist.')

    def deposit(self, accountType, amount):
        check_result = self.checkAccount(accountType)
        if check_result == 'account already exists':
            self.account_dictionary[accountType].deposit(amount)
        else:
            raise Exception('The account does not exist.')

    def withdraw(self, accountType, amount):
        check_result = self.checkAccount(accountType)
        if check_result == 'account already exists':
            self.account_dictionary[accountType].withdraw(amount)
        else:
            raise Exception('The account does not exist.')


    def __str__(self):
        summary = ['Owner: ', self.owner, '\n']
        if hasattr(self, 'account_dictionary'):
            for var in self.account_dictionary.items():
                summary += [str(var[0]), ': The balance is ', str(var[1].balance),'. \n']
        else:
            summary += 'No account is found.'
        return ''.join(summary)


def ATMSession(bankUser):
    def Interface():
        while True:
            main_option = input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n")
            main_option = int(main_option)
            if (main_option == 1):
                sys.exit()
            elif (main_option == 2):
                account_type_input = input("Enter Option:\n1)Checking\n2)Savings\n")
                account_type_input = int(account_type_input)
                if (account_type_input == 1):
                    bankUser.addAccount(AccountType.CHECKING)
                elif (account_type_input == 2):
                    bankUser.addAccount(AccountType.SAVINGS)
                else:
                    print("Your input is not valid.")
            elif (main_option == 3):
                account_type_input = input("Enter Option:\n1)Checking\n2)Savings\n")
                account_type_input = int(account_type_input)
                if (account_type_input == 1):
                    bankUser.getBalance(AccountType.CHECKING)
                elif (account_type_input == 2):
                    bankUser.getBalance(AccountType.SAVINGS)
                else:
                    print("Your input is not valid.")
            elif (main_option == 4):
                account_type_input = input("Enter Option:\n1)Checking\n2)Savings\n")
                account_type_input = int(account_type_input)
                input_amount = input("Enter Integer Amount, Cannot Be Negative:\n")
                input_amount = int(input_amount)
                if (account_type_input == 1):
                    bankUser.deposit(AccountType.CHECKING, input_amount)
                elif (account_type_input == 2):
                    bankUser.deposit(AccountType.SAVINGS, input_amount)
                else:
                    print("Your input is not valid.")
            elif (main_option == 5):
                account_type_input = input("Enter Option:\n1)Checking\n2)Savings\n")
                account_type_input = int(account_type_input)
                input_amount = input("Enter Integer Amount, Cannot Be Negative:\n")
                input_amount = int(input_amount)
                if (account_type_input == 1):
                    bankUser.withdraw(AccountType.CHECKING, input_amount)
                elif (account_type_input == 2):
                    bankUser.withdraw(AccountType.SAVINGS, input_amount)
                else:
                    print("Your input is not valid.")
            else:
                print("Your input is not valid.")
        return None
    return Interface

x = ATMSession(BankUser('Joe'))
x()
