# P5b

def make_withdrawal(balance):
    def cal_new_balance(withdraw):
        # to get the updated balance
        balance_after_last_withdraw = balance

        if balance_after_last_withdraw < 0:
            print('The balance is invalid.')
            return None
        if balance_after_last_withdraw == 0:
            print('Your balance is 0.')
            return None
        if balance_after_last_withdraw < withdraw:
            print('The withdraw amount is more than what you have now.')
            return None

        balance_after_current_withdraw = balance_after_last_withdraw - withdraw
        return balance_after_current_withdraw
    return cal_new_balance

print('The following code does not work because we only use the value of balance, but we do not update the global value of it, as we only change its value locally.')

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
