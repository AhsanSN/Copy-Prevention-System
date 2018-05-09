import pickle,pprint,socket,webbrowser,re
import sys, os

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

def encrypt_ip(ip):
    parts = []
    ip = ip+'.'
    word=''
    for a in ip:
        if (a!='.'):
            word = word+a
        if (a=='.'):
            parts.append(word)
            word=''
    for i in range (0, len(parts)):
        parts[i] = encrypt_number(int(parts[i]))
    return (parts)

    
def decrypte_ip(parts):
    for i in range (0, len(parts)):
        parts[i] = decrypte_number(int(parts[i]))
    retIp = str(parts[0]) + '.' +str(parts[1]) + '.'+str(parts[2]) + '.'+str(parts[3])
    return(retIp)
    
    


    
def activation():
    pkl_file = open('bin/data.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    # get allow value
    allow = (data1['allow'])
    key = int(input('Enter your Activation key: '))
    url = 'https://www.anomoz.com/license_verification.php?license='+str(key)
    webbrowser.open(url, new=2)
    confirmationKey = int(input('Enter your Confirmation key: '))
    #for trial
    '''
    key = 353375
    confirmationKey = 3580864
    '''
    if (allow==1):
        decKey=encrypt_number(key)
    if (allow==0):
        decKey=2 #used
        print('The key has been used.')
    print('decKey = '+str(decKey))
    print('confirmationKey = '+str(confirmationKey))
    if (confirmationKey == decKey):
        ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip.connect(("8.8.8.8", 80))
        macAddress=encrypt_ip(ip.getsockname()[0]) # local host ip address
        data1 = {'macAddress': macAddress, 'allow': 0}
        output = open('bin/data.pkl', 'wb')
        pickle.dump(data1, output)
        output.close()
        print('Your licence has been valiated. You can now use the software even if you are offline')
    if (confirmationKey != decKey):
        print('The entered Confirmation key was either invalid or has been used.')
    print('')
    a= input("Press any key to exit...")

############
    '''
data1 = {'macAddress': 0,
         'allow': 1
         }

output = open('bin/data.pkl', 'wb')
pickle.dump(data1, output)
output.close()
'''
###


'''main'''

def main():
    #styling
    print("-------------------------------------------------------------------------")
    print("                                LICENCE                                  ")
    print("-------------------------------------------------------------------------")
    #store mac address
    pkl_file = open('bin/data.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    storedMacAddress = decrypte_ip(data1['macAddress'])
    # get allow value
    allow = (data1['allow'])
    #current mac addresss
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    currentMacAddress=(ip.getsockname()[0]) # local host ip address

    if ((storedMacAddress != 0) and(storedMacAddress == currentMacAddress)):
        print("Your licence is registered :)")
    else:
        activation()
    
'''RUNNING'''
main()



