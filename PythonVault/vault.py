
#Austin Peterson
#Mr. Willis
#H Computer Programming 1-2, Pd.3

#This program is designed to handle mock bank accounts.
#It begins by welcoming the user to PythonVault banking,
#and then prompts them with their options of interactions
#with their money. After an option is selected, the program
#asks the user for their existing PIN. Using this PIN, the
#Program reads the user's data off of their existing PIN file.
#This allows the program access of the user's name and balance.
#If a new user does not currently have an existing account,
#they can choose to create a new one via the joinVault method.
#The transactions that can be performed with PythonVault's
#accounts are: withdraw, deposit, getBalance and checkBalance.
#if the user attempts to withdraw more than they currently have
#in their account, the program will return a message alerting
#the user of this mistake and charging a 10 dollar fee for
#the bouncing withdrawl. All accounts can be written over.

import time

class vaultFile:                                                                                    #class that manages writng account files
    def writeBalance(self,PIN,name,balance):
        account = open(str(PIN)+'.txt','w')                                                         #opens account file for rewriting of contents
        account.write(name)                                                                         #rewrites user's name in account file
        account.write('\n')                                                                         #creates new line in account file
        account.write(str(balance))                                                                 #writes new balance in accounts
        account.write('\n')
        account.close()                                                                             #closes account file

class vaultOperations:                                                                              #class that manages transactions
	def joinVault(self):
        name = raw_input ("please enter your name: ")                                               #takes new user's name for storage
        PIN = input ("Please enter your desired PIN: ")                                             #takes user's desired PIN for storage
        balance = input ("What is your beginning balance?: ")                                       #takes users beginning balance for storage
        vf = vaultFile()                                                                            #assigns vaultFile object to variable vf
        vf.writeBalance(PIN,name,balance)                                                           #calls method to write account file
        time.sleep(1)
        print("Your account has been saved.")                                                       #assures user their account creation was sucessful (always is.)
        time.sleep(.5)

    def withdraw(self):
        PIN = input ("Please enter your existing PIN: ")
        account = open(str(PIN)+'.txt','r+')                                                        #opens user's account file for both reading and rewriting
        lines = account.readlines()                                                                 #reads lines of file
        name = lines[0][:-1]                                                                        #assigns user's name in account file to variable
        currentbal = int(lines[1][:-1])                                                             #assigns user's current balance in account file to variable
        transamount = input("Hello "+name+".  Your balance is "+str(currentbal)+" dollars. \
            How much would you like to withdraw? ")                                                 #echo prints user's current balance, asks user how much they would like to withdraw
        newbalance = (currentbal-transamount)                                                       #subtracts desired withdrawl from currentbalance to create new balance
        time.sleep(.5)
        account.close()
        if newbalance>=0:
                vf = vaultFile()                                                                    #assigns vaultFile object to variable vf
                vf.writeBalance(PIN,name,balance)                                                   #calls method to write account file
                print(name+", your new total balance comes to a total of "+str(newbalance)+" \
                    dollars.")                                                                      #prints user's new balance
                time.sleep(1)
        else:
                vf = vaultFile()                                                                    #assigns vaultFile object to variable vf
                vf.writeBalance(PIN,name,balance)                                                   #calls method to write account file
                print(name+", you have insufficient funds for that withdrawal. \
                    10 dollar fee deducted.")                                                       #if the new total balance is less than zero,
                time.sleep(1)                                                                       #the transaction cannot be performed, $10 fee charged

	def deposit(self):
        PIN = input ("Please enter your existing PIN: ")
        account = open(str(PIN)+'.txt','r+')                                                        #opens account file for both reading ad rewriting
        lines = account.readlines()                                                                 #reads lines of file
        name = lines[0][:-1]                                                                        #assigns user's name in account file to variable
        currentbal = int(lines[1][:-1])                                                             #assigns user's current balance in account file to variable
        depositamount = input("Hello "+name+".  Your balance is "+str(currentbal)+" dollars. \
            How much would you like to deposit? ")                                                  #echo prints user's current balance, asks user how much they would like to withdraw
        newbalance = str(currentbal+depositamount)                                                  #creates new balance after deposit
        vf = vaultFile()                                                                            #assigns vaultFile object to variable vf
        vf.writeBalance(PIN,name,balance)                                                           #calls method to write account file
        time.sleep(.5)
        print(name+", your new total balance comes to a total of "+newbalance+" dollars.")          #prompts user of their new total balance in account
        time.sleep(1)

	def getBalance(self):
        PIN = input ("Please enter your existing PIN: ")
        account = open(str(PIN)+'.txt','r')                                                         #opens account file for reading only
        lines = account.readlines()                                                                 #reads lines of file
        name = lines[0][:-1]                                                                        #assigns user's name in account file to variable
        currentbal = int(lines[1][:-1])                                                             #assigns user's current balance in account file to variable
        print "Hello "+name+".  Your balance is "+str(currentbal)+" dollars."                       #prompts user of their current balance
        account.close()

	def checkBalance(self):
        PIN = input ("Please enter your existing PIN: ")
        account = open(str(PIN)+'.txt','r')                                                         #opens account for reading
        lines = account.readlines()                                                                 #reads lines in file
        name = lines[0][:-1]                                                                        #assigns user's name in account file to variable
        currentbal = int(lines[1][:-1])                                                             #assigns user's current balance in account file to variable
        if currentbal > 0:
                print name+(", your balance greater than zero.")
        else:
                print("Balance is less than zero.")

    def quit(self):
        print("Your money's safe with us, goodbye.")
        time.sleep(.5)
        break

    def invalidInput(self):
        print("Sorry, That is not valid input.")
        time.sleep(.5)

print """           
 _____     _   _              _____         _ _   
|  _  |_ _| |_| |_ ___ ___   |  |  |___ _ _| | |_ 
|   __| | |  _|   | . |   |  |  |  | .'| | | |  _|
|__|  |_  |_| |_|_|___|_|_|   \___/|__,|___|_|_|  
      |___|                                                                              
-Austin Peterson

"""                                                                                                 #prints Python Vault title banner

print("Hello and Welcome to Python Vault.")                                                         #greets user

time.sleep(1)

myVault = Vaultoperations()                                                                         #assigns Vaultoperations to variable myVault
while 1:
        transaction = raw_input("Would you like to: (j)-join python vault  \
            (w)-withdraw money  (d)-deposit money  (g)-get balance  (c)-check balance  (q)-quit")   #prompts user of transaction choices

        if transaction == 'j':
            myVault.joinVault()

        elif transaction == 'd':
            myVault.deposit()

        elif transaction == 'w':
            myVault.withdraw()

        elif transaction == 'g':
            myVault.getBalance()
                
        elif transaction == 'c':
            myVault.checkBalance()
                
        elif transaction == 'q':
            myVault.quit()
        else:
            myVault.invalidInput()
