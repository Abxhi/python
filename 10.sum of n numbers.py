a=int(input("Enter the nth-term to find sum : "))
if a < 0:
  print("Wrong Input")
else:
  sum=0
  for i in range(1,a+1):
    sum+=i
    
print("The sum is:", sum)
