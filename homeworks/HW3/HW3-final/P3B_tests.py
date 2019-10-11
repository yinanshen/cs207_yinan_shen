from Bank import AccountType
from Bank import BankAccount
from Bank import BankUser

# Case 1. over withdrawal
def test_over_withdrawal():
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS) 
    user.deposit(AccountType.SAVINGS, 10)
    try:
        user.withdraw(AccountType.SAVINGS, 1000)
    except Exception as exp:
        print(exp)
test_over_withdrawal()

# Case 2. deposit a negative amount of money
def test_deposit_negative():
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        user.deposit(AccountType.SAVINGS, -100)
    except Exception as exp:
        print(exp)
test_deposit_negative()

# Case 3. withdraw a negative amount of money
def test_withdraw_negative():
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        user.withdraw(AccountType.SAVINGS, -1)
    except Exception as exp:
        print(exp)
test_withdraw_negative()

# Case 4. no account is found
def test_no_account():
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        user.deposit(AccountType.CHECKING, 100)
    except Exception as exp:
        print(exp)
test_no_account()
