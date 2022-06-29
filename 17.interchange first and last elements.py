l=list(input("Enter a list: "))
print("Initial List : ",l)
length = len(l)
t=l[0]
l[0]=l[length - 1]
l[length - 1] = t

print("List after Swapping : ",l)
