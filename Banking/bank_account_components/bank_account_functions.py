'''

Description:  This module will house the bank account program
functions, including reading in the original file and storing
the accounts in memory as objects in a data type.

'''

#import regular expression module to extract text from a string
import re

#import bank account class from bank_account_class module
from . import bank_account_class as bank_class


#from fractions library, import Fraction for greater number precision
from fractions import Fraction


def read_file(file_name):

	'''

	reads the file and creates a dictionary with the key as the account
	and the value as the account object

	returns dictionary specified above

	'''

	acc_obj_dict = {}

	with open(file_name, 'r') as account:

		for line in account:

			acc_name = re.findall('(^.*):', line)[0]
			acc_bal = float(re.findall(': (.*\S)', line)[0])

			acc_obj_dict[acc_name] = bank_class.Bank_Account(acc_name, acc_bal)

	return acc_obj_dict

def welcome():

	'''

	User decides what user wishes to do with program

	'''

	print("\n\n1: View Balances\n2: Add Account")
	print("3: Deposit\n4: Withdraw\n5: Transfer")
	print("6: Remove Account\n7: Total Balance")
	print("8: Exit\n\nChoose an option:\n")

def user_choice():

	'''

	gets a valid choice from user (number b/w 1 and 7)

	'''

	while(True):

		choice = input()

		try:

			choice = int(choice)

		except:

			print("Please enter a number between 1 and 8")
			welcome()
			continue

		if(choice > 8 or choice < 1):

			print("Number must be between 1 and 8")
			welcome()
			continue

		print("\n")
		return choice

def view_bal(acc_obj_dict):

	'''

	allows user to see account balances altogether

	'''

	for key in acc_obj_dict:

		print(key, "$%.2f" % (acc_obj_dict[key].balance))

def add_acc(acc_obj_dict):

	'''

	allows user to add an account, asking for name and initial deposit

	'''

	acc_name = input("What is the name of your account?\t")

	acc_init_dep = input("How much is your initial deposit?\t")

	while(True):

		try:

			acc_init_dep = float(acc_init_dep)
			break

		except:

			acc_init_dep = input("Initial deposit must be a dollar amount, to the nearest cent.\n\n"\
			"How much is your initial deposit?\t")
			continue

	acc_obj_dict[acc_name] = bank_class.Bank_Account(acc_name, acc_init_dep)

def bank_dep(acc_obj_dict):

	'''

	allows user to deposit money to an account

	'''

	acc_name = input("What is the name of the account in which you wish to deposit your money?\n\n")

	while(acc_name not in acc_obj_dict.keys()):

		acc_name = input("%s not a valid account name.  In what account do you wish to deposit your money?\n\n"\
		% (acc_name))

	acc_dep = input("How much are you depositing?\t")

	while(True):

		try:

			acc_dep = float(acc_dep)
			break

		except:

			acc_dep = input("Deposit must be a dollar amount, to the nearest cent.\n\n"\
			"How much are you depositing?\t")
			continue

	acc_obj_dict[acc_name].deposit(acc_dep)

def bank_withdraw(acc_obj_dict):

	'''

	allows user to withdraw money from an account

	'''

	acc_name = input("What is the name of the account from which you wish to withdraw your money?\n\n")

	while(acc_name not in acc_obj_dict.keys()):

		acc_name = input("%s not a valid account name.  From what account do you wish to withdraw your money?\n\n"\
		% (acc_name))

	acc_wdraw = input("How much are you withdrawing?\t")

	while(True):

		try:

			acc_wdraw = float(acc_wdraw)
			break

		except:

			acc_wdraw = input("Withdrawal must be a dollar amount, to the nearest cent.\n\n"\
			"How much are you withdrawing?\t")
			continue

	while(acc_wdraw > acc_obj_dict[acc_name].balance):

		acc_wdraw = input("Insufficient funds.\n\n"\
		"How much are you withdrawing?\t")

		try:

			acc_wdraw = float(acc_wdraw)
			continue

		except:

			acc_wdraw = input("Withdrawal must be a dollar amount, to the nearest cent.\n\n"\
			"How much are you withdrawing?\t")
			continue

	acc_obj_dict[acc_name].withdraw(acc_wdraw)

def bank_transfer(acc_obj_dict):

	'''

	allows user to transfer money from one account to another

	'''

	acc_frm = input("What is the name of the account from which you wish to transfer your money?\n\n")

	while(acc_frm not in acc_obj_dict.keys()):

		acc_frm = input("%s not a valid account name.  From what account do you wish to transfer your money?\n\n"\
		% (acc_frm))

	acc_to = input("What is the name of the account to which you wish to transfer your money?\n\n")

	while(acc_to not in acc_obj_dict.keys()):

		acc_to = input("%s not a valid account name.  To what account do you wish to transfer your money?\n\n"\
		% (acc_to))

	acc_trsf = input("How much are you transferring?\t")

	while(True):

		try:

			acc_trsf = float(acc_trsf)
			break

		except:

			acc_trsf = input("Trasfer must be a dollar amount, to the nearest cent.\n\n"\
			"How much are you transferring?\t")
			continue

	while(acc_trsf > acc_obj_dict[acc_frm].balance):

		acc_trsf = input("Insufficient funds.\n\n"\
		"How much are you transferring?\t")

		try:

			acc_trsf = float(acc_trsf)
			continue

		except:

			acc_trsf = input("Transfer must be a dollar amount, to the nearest cent.\n\n"\
			"How much are you transferring?\t")
			continue

	acc_obj_dict[acc_frm].transfer(acc_obj_dict[acc_to], acc_trsf)

def remove_acc(acc_obj_dict):

	'''

	allows user to remove account, asking for name and where to transfer remaining money

	'''

	acc_remove = input("What is the name of the account you wish to remove?\n\n")

	while(acc_remove not in acc_obj_dict.keys()):

		acc_remove = input("%s not a valid account name.  Which account do you wish to remove?\n\n"\
		% (acc_remove))

	acc_to = input("You have $%.2f remaining in your %s account.  To which account would you like to transfer this money?\n\n"\
	% (acc_obj_dict[acc_remove].balance, acc_remove))

	while(acc_to not in acc_obj_dict.keys()):

		acc_to = input("%s not a valid account name.  TO which account do you wish to transfer your remaining money?\n\n"\
		% (acc_to))

	acc_obj_dict[acc_remove].transfer(acc_obj_dict[acc_to], acc_obj_dict[acc_remove].balance)

	del(acc_obj_dict[acc_remove])

def bank_total(acc_obj_dict):

	'''

	allows user to view total amount of money among all accounts

	'''

	total = 0

	for acct in acc_obj_dict:

		total += acc_obj_dict[acct].balance

	print("The total amount among all your accounts is $%.2f" % (total))

def write_file(file_name, acc_obj_dict):

	'''

	overwrites existing bank account file with updated balances and accounts
	after deposits, withdraws, transfers, etc.

	'''

	with open(file_name, 'w') as account:

		for key in acc_obj_dict:

			account.write("%s: %.2f\n" % (key, acc_obj_dict[key].balance))