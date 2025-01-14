# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
st1 = str(input("Enter the string: "))
n= len(st1)
st2 = st1[-1] + st1[1:(n-1)] + st1[0]
print(st2)