'''

Description: Bank Account Class to be used in the bank account
program to track different acccounts with money in them, which
currently include online savings, fifth third savings + checking,
stocks, wallet.

This class will have three methods: deposit, withdraw, and transfer.

Each instance of this class will have a name to track which account
is which and a balance to keep track of total money amounts

'''


class Bank_Account():

	def __init__ (self, name, balance):

		'''

		defines the attributes of each class instance:

		name = name of the account
		balance = amount of money in the account

		'''

		self.name = name
		self.balance = balance


	def deposit(self, amount):

		'''

		allows user to deposit money to an account of their choice

		'''

		self.balance += amount

	def withdraw(self, amount):

		'''

		allows user to withdraw money from an account of their choice

		'''

		self.balance -= amount

	def transfer(self, account, amount):

		'''

		allows user to transfer money from one account to another

		'''

		self.balance -= amount
		account.balance += amount