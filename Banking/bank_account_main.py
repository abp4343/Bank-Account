'''

Description:  This file executes the bank account program
for the user.  This is the file that handles the
withdrawals, transfers, deposits, etc.

'''

#import bank accout class and functions from bank acc comps
from bank_account_components import bank_account_class as bank_class
from bank_account_components import bank_account_functions as bank_function


bank_account_obj = bank_function.read_file('bank_accounts.txt')

bank_function.welcome()
bank_function.user_choice()