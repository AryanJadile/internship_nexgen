# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 
# 'not'...'poor' substring with 'good'. Return the resulting string.

st1 = str(input("Enter the string: "))

a = st1.find('not')
b = st1.find('poor')

if b>a and b>0 and a>0:
    st1 = st1.replace(st1[a:(b+4)],'good')
    print(st1)
else:
    print(st1)