import rstr
import re 

regularExpression=input("Enter Regular Expression :\n")
print("Examples for this regular expression are :\n",rstr.xeger(regularExpression))
ch=input("do yo want to check specific string acceptance :Enter Y :\n")
if ch =='y' or ch=='Y':
        string=input("Enter a string please")
        if re.fullmatch(regularExpression,string):
            print("accepted ")
        else:
            print ("unaccepted ")
