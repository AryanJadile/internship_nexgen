# Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string.

st1 = str(input("Enter first string: "))
st2 = str(input("Enter second string: "))
st3 = st2[0]+st2[1]+st1[2:] + " " + st1[0]+st1[1]+st2[2:]
print(st3)