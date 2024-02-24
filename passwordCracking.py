from string import *  # used to get all ascii character
from itertools import product

all = ascii_letters + digits + punctuation  # from string package

print("Enter password of <4 characters to get faster...")
pin = input("Enter your password : ")

for j in product(all, repeat = len(pin)):
    search ="".join(j)
    ptr=open("Combination.txt","a")
    ptr.write(search)
    ptr.write("   ")
    if search==pin :
        print("Your password is : ",search)
        ptr.close()
        break
    