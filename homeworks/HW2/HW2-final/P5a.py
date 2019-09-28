# P5a

def make_withdrawal(balance):
    def cal_new_balance(withdraw):

        if balance < 0:
            print('The balance is invalid.')
            return None
        if balance == 0:
            print('Your balance is 0.')
            return None
        if balance < withdraw:
            print('The withdraw amount is more than what you have now.')
            return None

        balance = balance - withdraw
        return balance
    return cal_new_balance

print('The following code does not work because the balance can only be accessed but cannot be modified by the inner function')

withdraw = make_withdrawal(10)
print('After the first withdraw 2, our balance is ', withdraw(2))
print('After the second withdraw 5, our balance is ', withdraw(5))
# If the third withdraw is 8, then the balance should drop below 0 (3 - 8 < 0)
withdraw(8)

# Test negative withdraw
print('')
withdraw_negative = make_withdrawal(-1)
withdraw_negative(2)

# Test zero withdraw
print('')
withdraw_zero = make_withdrawal(0)
withdraw_zero(2)
