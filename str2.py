#write a program to count the frequency of each character in the string.

#using concept of strings and loops

st1 = str(input("Enter the string: "))   # Takes input from the user
res = "" # Initializes an empty string
for i in st1:  # Accesses each character in the string
    if i not in res:  # checks if it is present in the new string initiated
        count = 0  # Initially the count is zero
        for j in st1: # Acts as another pointer
            if j == i: # Checks if both the values are same
                count+=1 # if the condition is true, then increments the counter
        
        res += f"{i}:{count}, " 

print(res.strip(", "))


