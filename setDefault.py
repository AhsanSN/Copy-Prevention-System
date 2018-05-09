import pickle,pprint,socket,webbrowser,re
import sys, os
############
    
data1 = {'macAddress': ['0','0','0','0'],
         'allow': 1,
         'trand':1
         }

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
output.close()

###
