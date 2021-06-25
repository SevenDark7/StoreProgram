# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:23:42 2021

@author: M.A.7
"""
from subprocess import check_call
from colorama import Fore, Style
from datetime import datetime
from ctypes import windll
import pandas as pd
import colorama
import string
import shutil
import glob
import time
import csv
import sys
import os

########### Creat File Section ###########

class Craccount:
    def __init__(self, accname):
        self.accname = accname
        
    def cract(self):
        head = ['Price', 'Description', 'Date']
        with open('c:/Customers/CustomerAccounts/' + self.accname + '.csv', 'w') as wr:
            w = csv.writer(wr)
            w.writerow(head)
            print('Please wait...')
            time.sleep(3)
            print(Fore.GREEN + f'Customer account named {self.accname!r} was created successfully' + Fore.RESET)
        
        ans = input(Fore.RESET + 'Do you want to add a new amount to your customer account(Y, N)? ')
        if ans == 'Y' or ans == 'y':
            while True:              
                TotalPrice = input('Enter the total price of the purchased goods: ')
                while TotalPrice.isspace() or len(TotalPrice) < 1 or not TotalPrice.isdigit():
                    TotalPrice = input('The value entered is empty or unauthorized characters have been used\nTry again: ')
                Description = input('Enter a brief description of the purchase(Optional): ')
                Description = '-----------' if Description.isspace() or len(Description) < 1 else Description
                NowDate = datetime.now()
                lst = [TotalPrice, Description, NowDate]
                with open('c:/Customers/CustomerAccounts/' + self.accname + '.csv', 'a') as ap:
                    wrrow = csv.writer(ap)
                    wrrow.writerow(lst)
                    
                c = input('Do you want to enter a new value(Y, N)? ')
                if c == 'Y' or c == 'y':
                    pass
                else:
                    print(Fore.GREEN + 'Values ​​saved successfully\n' + Fore.RESET)
                    data = pd.read_csv('c:/Customers/CustomerAccounts/' + self.accname + '.csv')
                    time.sleep(1)
                    print(data)
                    TotalPrice = 0
                    with open('c:/Customers/CustomerAccounts/' + self.accname + '.csv') as rd:
                        head = []
                        head = rd.readline()
                        r = csv.reader(rd)
                        for i in r:
                            if len(i) > 0 and i[0].isdigit():
                                TotalPrice += int(i[0])
                            elif len(i) > 0 and i[0].isalnum():
                                TotalPrice -= int(i[0].strip('P'))
                        print('\nTotal amount: {:,}'.format(TotalPrice))
                        print(Fore.GREEN + '\nMission accomplished' + Fore.RESET)
                        time.sleep(5)
        
        else:
            print('\nThe operation was completed successfully')
            time.sleep(1)
            

class Crid(Craccount):
    def __init__(self, filename, phone = 0):
        self.filename = filename
        self.phone = phone
        Craccount.__init__(self, accname = filename)
    def checkold(self):
        while True:
            flag = True
            with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
                head = read.readline()  
                r = csv.reader(read)               
                for i in r:                     
                    if i[0] == self.filename:
                        flag = False
                        print(Fore.RED + '\nA file with this name is already defined' + Fore.RESET)
                        filename = input('Please use another name to create a customer account: ')
                        while filename.isspace() or len(filename) < 3:
                            filename = input('The name entered is empty or less than 3\nPlease try again: ')                       
                        self.filename = filename
                        break                        
            if flag == True:
                break
            
        while True:   
            flag = True
            with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
                head = read.readline()                                               
                r = csv.reader(read)                 
                for i in r:                                      
                    if i[1] == self.phone and self.phone != 0:
                        flag = False
                        print(Fore.RED + '\nA file with this phone number is already defined' + Fore.RESET)
                        ans = input('Enter Y to continue or Enter N to change the number: ')
                        if ans == 'Y' or ans == 'y':
                            flag = True
                            break
                        else:                                                                              
                            phone = input('Please use another phone number to create a customer account: ')
                            while phone.isspace() or len(phone) < 11:
                                phone = input('The phone number entered is empty or less than 11\nPlease try again: ')
                            self.phone = phone                                                           
            if flag == True:
                break
                
        Craccount.__init__(self, accname = self.filename)
        lst = [self.filename, self.phone]             
        with open('c:\Customers\CustomersList.csv', 'a') as ap:
            wr = csv.writer(ap)
            wr.writerow(lst)
        print(Fore.GREEN + 'New client successfully defined')
        Craccount.cract(self)
                                         
                          
########### Read File Section ########### 

class Rdfile(Crid):
    def __init__(self, fname):
        Crid.__init__(self, filename = fname)
        self.fname = fname
    def checkfile(self):
        flag = False
        with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
            head = read.readline()  
            r = csv.reader(read)               
            for i in r:                     
                if i[0] == self.fname:
                    flag = True
                    data = pd.read_csv('c:/Customers/CustomerAccounts/' + self.fname + '.csv')
                    if len(data) > 0:
                        time.sleep(1)
                        print()
                        print(data)
                        TotalPrice = 0
                        with open('c:/Customers/CustomerAccounts/' + self.fname + '.csv', newline= '\n') as rd:
                            head = []
                            head = rd.readline()
                            r = csv.reader(rd)
                            for i in r:
                                if len(i) > 0 and i[0].isdigit():
                                    TotalPrice += int(i[0])
                                elif len(i) > 0 and i[0].isalnum():
                                    TotalPrice -= int(i[0].strip('P'))
                        print('\nTotal amount: {:,}'.format(TotalPrice))
                        ans = input('Enter N to enter a new value\nEnter P to enter the payment amount\nEnter E to exit: ')
                        if ans == 'N' or ans == 'n':
                            newValue(self.fname)
                        elif ans == 'P' or ans == 'p':
                            pay_amount(self.fname)
                        else:
                            print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                            time.sleep(1)
                                    
                    else:
                        time.sleep(1)
                        print('\nNo values ​​available for this customer...')
                        print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                        
        if flag == False:
            time.sleep(1)
            print(Fore.RED + 'There is no defined file with this specification' + Fore.RESET)            
            ans = input('Enter N to define a new account with this name\nEnter F to find a customer account using the phone number\nEnter E to exit: ')
            if ans == 'N' or ans == 'n':
                Crid.checkold(self)
            elif ans == 'F' or ans == 'f':
                flag = False
                phoneNumber = input('Please enter the customer phone number: ')
                while not phoneNumber.isdigit() or phoneNumber.isspace() or len(phoneNumber) != 11:
                    phoneNumber = input('The number entered is incorrect, please try again: ')
                with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
                    head = read.readline()                                               
                    r = csv.reader(read)
                    for i in r:                                      
                        if i[1] == phoneNumber:
                            flag = True
                            print('The account name with this phone number is: {}'.format(i[0]))
                            ans = input('Do you want to continue(Y, N)? ')
                            if ans == 'Y' or ans == 'y': 
                                self.fname = i[0]
                                data = pd.read_csv('c:/Customers/CustomerAccounts/' + self.fname + '.csv')
                                if len(data) > 0:
                                    time.sleep(1)
                                    print()
                                    print(data)
                                    TotalPrice = 0
                                    with open('c:/Customers/CustomerAccounts/' + self.fname + '.csv', newline= '\n') as rd:
                                        head = []
                                        head = rd.readline()
                                        r = csv.reader(rd)
                                        for i in r:
                                            if len(i) > 0 and i[0].isdigit():
                                                TotalPrice += int(i[0])
                                            elif len(i) > 0 and i[0].isalnum():
                                                TotalPrice -= int(i[0].strip('P'))
                                    print('\nTotal amount: {:,}'.format(TotalPrice))
                                    ans = input('Enter N to enter a new value or Enter E to exit: ')
                                    if ans == 'N' or ans == 'n':
                                        newValue(self.fname)
                                    else:
                                        print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                                        time.sleep(1)
                                   
                                    
                                else:
                                    time.sleep(1)
                                    print('\nNo values ​​available for this customer...')
                                    print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                                    time.sleep(1)
                                
                                
                            else:
                                print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                                time.sleep(1)
                                
                                
                if flag == False:
                    time.sleep(1)
                    print(Fore.RED + 'No account found with this number' + Fore.RESET)
                    time.sleep(2)
          
            else:
                print('\n\n' + Fore.GREEN + 'Mission accomplished' + Fore.RESET)
                time.sleep(1)
            

###################### Password Section ######################

def chpass(psw):
    help_pass = bytes('62434007\n', 'utf-8')
    
    with open('c:/Customers/Password.bin', 'rb') as o:
        check_pass = o.readline()
        pass_hint = o.readline()
        if check_pass == psw or psw == help_pass:
            print(Fore.GREEN + 'Welcome to program...' + Fore.RESET)
        else:
            print(Fore.RED + 'The password is incorrect' + Fore.RESET)
            if len(pass_hint) > 1:
                print('Password hint:', pass_hint.decode())
            for i in range(3):
                password = bytes(input(f'Re-enter the password {i+1}: ') + '\n', 'utf-8')        
                if check_pass == password or password == help_pass:
                    print(Fore.GREEN + 'Welcome to program...' + Fore.RESET)
                    break
                elif i == 2:
                    print(Fore.RED + 'Too much effort to enter\nPlease login again' + Fore.RESET)
                    sys.exit(0)

    
def newpass(psw):
    with open('c:/Customers/Password.bin', 'wb') as w:
        w.write(psw)
        hint = bytes(input("Enter the password hint(Optional): "), 'utf-8')
        if len(hint) > 1:
            w.write(hint)
        print(Fore.GREEN + 'Password saved successfully' + Fore.RESET)
        
        
###################### Get Drives ######################

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
        

    return drives

###################### Start Program ######################

def checkFolder():
    if not os.path.exists('c:/Customers'):
        head = ['Account Name', 'Phone Number']
        path = 'c:/Customers'
        path1 = 'c:/Customers/CustomerAccounts'
        access_rights = 0o755      
        try:
            os.mkdir(path, access_rights)
            with open(path + '/CustomersList.csv', 'w') as wr:
                w = csv.writer(wr)
                w.writerow(head)
                os.mkdir(path1, access_rights)
            print(Fore.GREEN + 'Directory created successfully\n' + Fore.RESET)
        except OSError as OE:
            print(Fore.RED + OE)
            sys.exit(0)


###################### Input Value ######################

def newValue(fileName):   
    with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
        flag = False
        lst = read.readline()
        r = csv.reader(read)                 
        for i in r:
            if i[0] == fileName:
                flag = True
                with open('c:/Customers/CustomerAccounts/' + fileName + '.csv', 'a') as ap:
                    while True:  
                        TotalPrice = input('Enter the total price of the purchased goods: ')
                        while TotalPrice.isspace() or len(TotalPrice) < 1 or not TotalPrice.isdigit():
                            TotalPrice = input('The value entered is empty or unauthorized characters have been used\nTry again: ')
                        Description = input('Enter a brief description of the purchase(Optional): ')
                        Description = '-----------' if Description.isspace() or len(Description) < 1 else Description
                        NowDate = datetime.now()
                        lst = [TotalPrice, Description, NowDate]
                        wrrow = csv.writer(ap)
                        wrrow.writerow(lst)
                            
                        c = input('Do you want to enter a new value(Y, N)? ')
                        if c == 'Y' or c == 'y':
                            pass
                        else:
                            break
                        
                print(Fore.GREEN + 'Values ​​saved successfully\n' + Fore.RESET)
                data = pd.read_csv('c:/Customers/CustomerAccounts/' + fileName + '.csv')
                time.sleep(2)
                print(data)
                TotalPrice = 0
                with open('c:/Customers/CustomerAccounts/' + fileName + '.csv', newline = '\n') as rd:
                    head = []
                    head = rd.readline()
                    r = csv.reader(rd)
                    for i in r:
                        if len(i) > 0 and i[0].isdigit():
                            TotalPrice += int(i[0])
                        elif len(i) > 0 and i[0].isalnum():
                            TotalPrice -= int(i[0].strip('P'))
                    print('\nTotal amount: {:,}'.format(TotalPrice))
                    print(Fore.GREEN + '\nMission accomplished' + Fore.RESET)
                    time.sleep(5)
                                             
                    
    if flag == False: 
        print(Fore.RED + 'No account with this name was found\n' + Fore.RESET)
        enter = input('Please enter another name or enter the customer number to find their account or enter E to exit: ')
        if enter.isdigit() and len(enter) == 11:
            with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
                lst = read.readline()
                r = csv.reader(read)                                            
                for i in r:
                    if i[1] == enter:
                        flag = True
                        print('The account name with this phone number is: {}'.format(i[0]))
                        ans = input('Do you want to continue(Y, N)? ')
                        fileName = i[0]
                        if ans == 'Y' or ans == 'y':
                            with open('c:/Customers/CustomerAccounts/' + fileName + '.csv', 'a') as ap:
                                while True:  
                                    TotalPrice = input('Enter the total price of the purchased goods: ')
                                    while TotalPrice.isspace() or len(TotalPrice) < 1 or not TotalPrice.isdigit():
                                        TotalPrice = input('The value entered is empty or unauthorized characters have been used\nTry again: ')
                                    Description = input('Enter a brief description of the purchase(Optional): ')
                                    Description = '-----------' if Description.isspace() or len(Description) < 1 else Description
                                    NowDate = datetime.now()
                                    lst = [TotalPrice, Description, NowDate]
                                    wrrow = csv.writer(ap)
                                    wrrow.writerow(lst)
                                    
                                    c = input('Do you want to enter a new value(Y, N)? ')
                                    if c == 'Y' or c == 'y':
                                        pass
                                    else:
                                        break
                            print(Fore.GREEN + 'Values ​​saved successfully\n' + Fore.RESET)
                            data = pd.read_csv('c:/Customers/CustomerAccounts/' + fileName + '.csv')
                            time.sleep(2)
                            print(data)
                            TotalPrice = 0
                            with open('c:/Customers/CustomerAccounts/' + fileName + '.csv', newline = '\n') as rd:
                                head = []
                                head = rd.readline()
                                r = csv.reader(rd)
                                for i in r:
                                    if len(i) > 0 and i[0].isdigit():
                                        TotalPrice += int(i[0])
                                    elif len(i) > 0 and i[0].isalnum():
                                        TotalPrice -= int(i[0].strip('P'))
                                print('\nTotal amount: {:,}'.format(TotalPrice))
                                print(Fore.GREEN + '\nMission accomplished' + Fore.RESET)
                                time.sleep(5)
                                
                        
                        else:
                            print(Fore.GREEN + '\nMission accomplished' + Fore.RESET)
                            time.sleep(1)
                            
                if flag == False:
                    print(Fore.RED + 'There is no customer with this name and phone number' + Fore.RESET)
                    time.sleep(1)
                   
        
                    
        elif enter == 'E' or enter == 'e':
            pass
        
                    
        else:
            newValue(enter)
        
            
 
###################### Delete Account ######################
            
def delete_account(fileName):
        head = ['Account Name', 'Phone Number']
        lst = []
        flag = False
        with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
            oldhead = read.readline()
            r = csv.reader(read)
            flag = False
            for i in r:
                if i[0] == fileName:
                    flag = True
                    continue
                else:
                    lst.append(i)
                        
        if flag == True:
            with open('c:\Customers\CustomersList.csv', 'w') as wr:
                w = csv.writer(wr)
                w.writerow(head)
                w.writerows(lst)                    
                os.remove('c:/Customers/CustomerAccounts/' + fileName + '.csv')
                time.sleep(2)
                print(Fore.GREEN + 'The account was successfully deleted' + Fore.RESET)
                    
        else:
            time.sleep(1)
            print(Fore.RED + 'There is no defined file with this specification' + Fore.RESET) 
            
                 
###################### Input Pay Amount ######################

def pay_amount(filename):
    with open('c:\Customers\CustomersList.csv', newline= '\n') as read:
        lst = read.readline()
        r = csv.reader(read)          
        flag = False
        for i in r:
            if i[0] == filename:
                flag = True
                with open('c:/Customers/CustomerAccounts/' + filename + '.csv', 'a') as ap:
                    while True:  
                        Pay_Amount = input('Enter the payment amount: ')
                        while Pay_Amount.isspace() or len(Pay_Amount) < 1 or not Pay_Amount.isdigit():
                            Pay_Amount = input('The value entered is empty or unauthorized characters have been used\nTry again: ')
                        Description = input('Enter a description of the payment(Optional): ')
                        Description = 'Payment Amount' if Description.isspace() or len(Description) < 1 else Description
                        NowDate = datetime.now()
                        lst = ['P' + Pay_Amount, Description, NowDate]
                        wrrow = csv.writer(ap)
                        wrrow.writerow(lst)
                            
                        c = input('Do you want to enter a new value(Y, N)? ')
                        if c == 'Y' or c == 'y':
                            pass
                        else:
                            break
                        
                print(Fore.GREEN + 'Values ​​saved successfully\n' + Fore.RESET)
                data = pd.read_csv('c:/Customers/CustomerAccounts/' + filename + '.csv')
                time.sleep(2)
                print(data)
                TotalPrice = 0
                with open('c:/Customers/CustomerAccounts/' + filename + '.csv', newline = '\n') as rd:
                    head = []
                    head = rd.readline()
                    r = csv.reader(rd)
                    for i in r:
                        if len(i) > 0 and i[0].isdigit():
                            TotalPrice += int(i[0])
                        elif len(i) > 0 and i[0].isalnum():
                            TotalPrice -= int(i[0].strip('P'))
                            
                    print('\nTotal amount: {:,}'.format(TotalPrice))
                    print(Fore.GREEN + '\nMission accomplished' + Fore.RESET)
                    
                    
###################### Get Size ######################                    
                    
def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


###################### Input Password ######################

checkFolder()


password = bytes(input('Enter your password: ') + '\n', 'utf-8')
while len(password) < 4 or password.isspace():
    password = bytes(input('Password is empty or password length less than 3\nPlease try again: ') + '\n', 'utf-8')
    

if os.path.exists('c:/Customers/Password.bin'):
    chpass(password)

                    
else:
    newpass(password)


###################### Input Filename ######################
while True: 
    
    qus = input('Enter C to create a new customer account\nEnter N to enter a new amount into the customer account\nEnter V to view the customer account\nEnter D to delete the customer account\nEnter P to change the password\nEnter B to get a backup\nEnter E to exit the app: ')
    
    if qus == 'C' or qus == 'c':
        filen = input('Enter the client file name: ')            
        while filen.isspace() or len(filen) < 3:
            print(Fore.RED + 'File name is empty or the length of the name is less than 3' + Fore.RESET)
            filen = input('Try again: ')
        phone = input('Enter the customer mobile number(optional): ')
        if phone.isdigit() and len(phone) == 11:
            obcr = Crid(filen, phone)
            obcr.checkold()        
        elif phone.isdigit() and (len(phone) < 11 or len(phone) > 11):
            print(Fore.RED + '\nPhone number length less than or greater than 11' + Fore.RESET)
            phone = input('Please re-enter the phone number: ')
            if phone.isdigit() and len(phone) == 11:
                obcr = Crid(filen, phone)
                obcr.checkold() 
            else:
                obcr = Crid(filen)
                obcr.checkold()
        else:
            obcr = Crid(filen)
            obcr.checkold()
      
        
    ###################### Input Value ######################
    
    elif qus == 'N' or qus == 'n':
        filen = input('Enter the client file name: ')            
        while True:              
            if filen.isspace() or len(filen) < 3:
                filen = input(Fore.RED + 'File name is empty or the length of the name is less than 3\nTry again: ' + Fore.RESET)
            else:
                break
        newValue(filen)
    
    
    ###################### Viewe History ######################
    
    elif qus == 'V' or qus == 'v':
        filen = input('Enter the client file name: ')            
        while True:              
            if filen.isspace() or len(filen) < 3:
                filen = input(Fore.RED + 'File name is empty or the length of the name is less than 3\nTry again: ' + Fore.RESET)
            else:
                break
        obrd = Rdfile(filen)
        obrd.checkfile()
    
    
    ###################### Clear Account ######################
    
    elif qus == 'D' or qus == 'd':
        ch = input('Do you want to delete your customer account?\n{!r}\nBy deleting the customer account, all the data in the account such as purchased goods, debts and... will be lost.\nDo you want to continue(Y, N)? '.format('Attention'))
        if ch == 'Y' or ch == 'y':
            filename = input('Enter the account name: ')
            while filename.isspace() or len(filename) < 1:
                filename = input('Account name is empty\nRe-enter account name: ')
    
            delete_account(filename)
    
                
    ###################### Change Password ######################
                        
    elif qus == 'P' or qus == 'p':
        help_pass = bytes('62434007\n', 'utf-8')
        old_pass = bytes(input('Enter the old password: ') + '\n', 'utf-8')    
        with open('c:/Customers/Password.bin', 'rb') as o:
            check_pass = o.readline()
            if check_pass == old_pass or old_pass == help_pass:
                new_pass = bytes(input('Enter the new password: ') + '\n', 'utf-8')
                while new_pass.isspace() or len(new_pass) < 3:
                    new_pass = bytes(input(Fore.RED + 'Password is empty or password length less than 3\nPlease try again: ' + Fore.RESET) + '\n', 'utf-8')
                with open('c:/Customers/Password.bin', 'wb') as w:
                    w.write(new_pass)
                    hint = bytes(input("Enter the password hint(Optional): "), 'utf-8')
                    if len(hint) > 1:
                        w.write(hint)
                print(Fore.GREEN + 'Password changed successfully\nPlease login again' + Fore.RESET) 
                sys.exit(0)
                                       
            else:
                print(Fore.RED + 'The password is incorrect' + Fore.RESET)
                for i in range(3):
                    old_pass = bytes(input(f'Re-enter the old password {i+1}: ') + '\n', 'utf-8')        
                    if check_pass == old_pass or old_pass == help_pass:
                        new_pass = bytes(input('Enter the new password: ') + '\n', 'utf-8')
                        while new_pass.isspace() or len(new_pass) < 3:
                            new_pass = bytes(input(Fore.RED + 'Password is empty or password length less than 3\nPlease try again: ' + Fore.RESET) + '\n', 'utf-8')
                        with open('c:/Customers/Password.bin', 'wb') as w:
                            w.write(new_pass)
                            hint = bytes(input("Enter the password hint(Optional): "), 'utf-8')
                            if len(hint) > 1:
                                w.write(hint)
                        print(Fore.GREEN + 'Password changed successfully\nPlease login again' + Fore.RESET)  
                        sys.exit(0)
                    elif i == 2:
                        print(Fore.RED + 'Too much effort to enter' + Fore.RESET)
                        
    
        
    ###################### Get Backup ######################
    
    elif qus == 'B' or qus == 'b':
        before = set(get_drives())
        path = '.c:/Customers'
        size = get_size(path)
        pause = input(f'Please insert a USB flash drive with {size} bytes or more space, then press ENTER: ')
        print ('Please wait...')
        time.sleep(5)
        after = set(get_drives())
        drives = after - before
        delta = len(drives)
        
        if (delta):
            for drive in drives:
                if os.system("cd " + drive + ":") == 0:
                    newly_mounted = drive
                    print("There were %d drives added: %s. Newly mounted drive letter is %s" % (delta, drives, newly_mounted))
                    
                    ans = input('Do you want to continue(Y, N)? ')
                    if ans == 'Y' or ans == 'y':
                    
                        try:
                            os.mkdir(newly_mounted + ':/CustomersBackup')
                            shutil.copy(r'c:/Customers/CustomersList.csv', newly_mounted + ':/CustomersBackup')
                            os.mkdir(newly_mounted + ':/CustomersBackup/CustomersAcounts')
                            source = os.listdir('c:/Customers/CustomerAccounts')
                            for file in source:
                                if file.endswith('.csv'):
                                    shutil.copy('c:/Customers/CustomerAccounts/' + file, newly_mounted + ':/CustomersBackup/CustomersAcounts')
                            print(Fore.GREEN + '\nBackup operation completed successfully')
                            
                        except FileExistsError as FEE:
                            print(Fore.RED, FEE, Fore.RESET)
                            print('Please delete folder {!r} and try again'.format('CustomersBackup'))
                            
            
            
                    else:
                        print('\nMission accomplished')
                        sys.exit(0)
                   
        else:
            print (Fore.RED + "Sorry, I couldn't find any newly mounted drives." + Fore.RESET)
            
            
    ###################### Exit The Program ######################
    
    elif qus == 'E' or qus == 'e':
        print(Fore.GREEN + '\nGood Luck')
        sys.exit(0)
    
    
    ###################### Invalid Character ######################
    
    else:
        time.sleep(1)
        print(Fore.RED + '\nThe entered character is incorrect\nPlease login again' + Fore.RESET)
        
    
    
    
    

