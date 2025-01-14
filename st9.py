# Write a  Python program to remove the nth index character from a nonempty string.
st1 = str(input("Enter the string: "))
n = int(input("Enter the index to be removed: "))
st2 = st1[0:n] + st1[(n+1):]
print(st2)