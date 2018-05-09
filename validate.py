import pickle,pprint,socket,webbrowser,re
import sys, os
# Save a dictionary into a pickle file.
'''main'''
    
def main():
    os.chdir(os.getcwd())
    #store mac address
    pkl_file = open('data.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    storedMacAddress = (data1['macAddress'])
    # get allow value
    allow = (data1['allow'])
    #current mac addresss
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    currentMacAddress=(ip.getsockname()[0]) # local host ip address

    if (storedMacAddress == 0):
        return False
    elif ((storedMacAddress != 0) and(storedMacAddress == currentMacAddress)):
        return True
    else:
        return False
    
'''RUNNING'''
main()
print('done')




