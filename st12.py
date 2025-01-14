# Write a Python program to count the occurrences of each word in a given sentence.
st1 = str(input("Enter the string: "))
st1 = st1.lower()
count = dict()

words = st1.split()
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    
print(count)
