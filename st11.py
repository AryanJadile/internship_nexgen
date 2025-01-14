# Write a Python program to remove characters that have odd index values in a given string.
st1 = str(input("Enter the string: "))
res = ""
for i in range(len(st1)):
    if i%2 == 0:
        res = res + st1[i]
    
print(res)