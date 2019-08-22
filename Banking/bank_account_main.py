'''

Description:  This file executes the bank account program
for the user.  This is the file that handles the
withdrawals, transfers, deposits, etc.

'''

#import bank accout class and functions from bank acc comps
from bank_account_components import bank_account_class as bank_class
from bank_account_components import bank_account_functions as bank_function


bank_account_obj = bank_function.read_file('bank_accounts.txt')

choice = 0

#while user does not wish to exit, loop
while(choice != 8):

	#ask for option
	bank_function.welcome()

	#get user choice
	choice = bank_function.user_choice()


	#with each choice, run necessary function, then continue
	if (choice == 1):

		bank_function.view_bal(bank_account_obj)
		continue

	elif (choice == 2):

		bank_function.add_acc(bank_account_obj)
		continue