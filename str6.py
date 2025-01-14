# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing', add 'ly' instead.
#  If the string length of the given string is less than 3, leave it unchanged.

st1 = str(input("Enter the string: "))
if len(st1)>=3:
    if st1[-3:] == "ing":
        st2 = st1 + "ly"

    elif str[-3:] != "ing":
        st2 = st1 + "ing"

else:
    print(st1)
