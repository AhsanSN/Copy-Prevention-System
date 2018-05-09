import pickle,pprint,socket,webbrowser,re, random,string
import sys, os
from random import *

# Save a dictionary into a pickle file.
'''
favorite_color = { "lion": "yellow", "kitty": "red" }
strings = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
pickle.dump( favorite_color, open( "save.p", "wb" ) )
pickle.dump( strings, open( "save.p", "wb" ) )
'''


def encrypt_number(inputnumber):
    plainText = inputnumber
    chtemp = plainText
    sumnum = ""
    length = len(str(plainText))
    for i in range (1,length+1):
        ch= chtemp%(10)
        if (ch == 1):
            rep = '5'
        elif (ch == 2):
            rep = '7'
        elif (ch == 3):
            rep = '2'
        elif (ch == 4):
            rep = '0'
        elif (ch == 5):
            rep = '8'
        elif (ch == 6):
            rep = '6'
        elif (ch == 7):
            rep = '1'
        elif (ch == 8):
            rep = '4'
        elif (ch == 9):
            rep = '3'
        elif (ch == 0):
            rep = '9'
        chtemp = chtemp //(10)
        sumnum += rep
        Number = int(sumnum )
        Reverse = 0    
        while(Number > 0):    
            Reminder = Number %10    
            Reverse = (Reverse *10) + Reminder    
            Number = Number //10         
    return (Reverse+3298646)
    
def decrypte_number(inputnumber):
    plainText = inputnumber-3298646
    chtemp = plainText
    sumnum = ""
    length = len(str(plainText))
    for i in range (1,length+1):
        ch= chtemp%(10)
        if (ch == 5):
            rep = '1'
        elif (ch == 7):
            rep = '2'
        elif (ch == 2):
            rep = '3'
        elif (ch == 1):
            rep = '7'
        elif (ch == 8):
            rep = '5'
        elif (ch == 6):
            rep = '6'
        elif (ch == 0):
            rep = '4'
        elif (ch == 4):
            rep = '8'
        elif (ch == 3):
            rep = '9'
        elif (ch == 9):
            rep = '0'
        chtemp = chtemp //(10)
        sumnum += rep
        Number = int(sumnum )
        Reverse = 0    
        while(Number > 0):    
            Reminder = Number %10    
            Reverse = (Reverse *10) + Reminder    
            Number = Number //10         
    return (Reverse)

lst = []
code=randint(10000, 9999999)
print(code)
ina = encrypt_number(code)
print(ina)
inb = decrypte_number(ina)
print(inb)
if (code == inb):
    print("this is good")
for i in range (0,20):
    code=randint(10000, 9999999)
    print(code)
    ina = encrypt_number(code)
    print(ina)
    inb = decrypte_number(ina)
    print(inb)
    if (code == inb):
        print("this is good")
        entery = '('+str(code)+','+str(ina)+')'
        lst.append(entery)

for a in lst:
    print(a)
    print('')




    
