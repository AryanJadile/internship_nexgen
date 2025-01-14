# Write a Python function that takes a list of words and return the longest word and the length of the longest one.

st1 = str(input("Enter the string: "))
l1 = st1.split(' ')
l1.sort(key=len)
print(l1[-1])