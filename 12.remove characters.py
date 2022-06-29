str =str(input("Enter any string"))
 
print(str.translate({ord(i): None for i in '123'}))
