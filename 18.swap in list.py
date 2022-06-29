def swapList(sl,pos1,pos2):
    n = len(sl)     
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl      

l=list(input("Enter a list: "))
pos1=int(input("Enter a 1st position: "))
pos2=int(input("Enter a 2nd position: ")) 

print(l)
print("Swapped list: ",swapList(l,pos1-1,pos2-1))
