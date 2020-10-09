
'''
Author: Aditya Mangal 
Date:  18 september,2020
Purpose: python mini project

'''
import time
import os
from win32com.client import Dispatch


def find_binod(filename):

    with open(filename, 'r') as f:
        file = f.read()
        for line in file:
            line = 0

            if 'binod' in file.lower():
                line += 1
                print(f'{line} found in {filename}.')
                return True

            else:
                return False


if __name__ == "__main__":
    speak = Dispatch('SAPI.spvoice')
    speak.speak('it is a Binod detector')
    file_path = input('Enter the full path of directory.\n')
    os.chdir(file_path)
    user_file = input(
        'Enter the full file name from which you want to find the binod.\n')
    print('Detecting binod please wait!')
    time.sleep(2)
    binod = find_binod(user_file)
    if(binod):
        print(f"binod found in {user_file}")

    else:
        print(f'Not found in {user_file}')
