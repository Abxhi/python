t=tuple()
num=int(input("Total number of values in tuple: "))
for i in range(num):
    x=input("enter element: ")
    t=t+(x,)
print("Max value: ",max(t))
print("Min value: ",min(t))
