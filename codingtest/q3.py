"""Write the code to Initialize a dictionary in python
and save json of the dictonary in a file?"""

exDict = {}
exDict['Priyanka']={
    'name':'Priyanka',
    'address':'Mumbai, MH',
    'phone':7709356993
    }
exDict['Avinash']={
    'name':'Avinash',
    'address':'Pimpri,Pune, MH',
    'phone':9092346534
    }

import json
s= json.dumps(exDict)
print(s)
with open("dictionary.txt","w") as f:
    f.write(s)
