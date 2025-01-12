# Write a Python program to get a string from a given
# string where all occurrences of its first char have been changed to '$', except the first char itself.

# st1 = str(input("Enter the string: "))
# res = ""
# n = len(st1)

# for i in range(1,n):
#     if st1[i]==st1[0]:
#         st2 = st1.replace(st1[i],"$")
#     else:
#         st2 = st1

# print(st2)             


st1 = str(input("Enter the string: "))
st2 = st1[0] + st1[1:].replace(st1[0],"$")
print(st2)