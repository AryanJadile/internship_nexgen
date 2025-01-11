#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
#If the string length is less than 2, return the empty string instead.

def new_str(inp_str):
    if len(inp_str)>=3:
        print(inp_str[0]+inp_str[1]+inp_str[-2]+inp_str[-1])
    elif len(inp_str)==2:
        print(inp_str+inp_str)
    else:
        print("Empty String")

a = str(input())
new_str(a)