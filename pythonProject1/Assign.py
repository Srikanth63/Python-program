#finding the smallest number from given three.
#using input function.
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the second number:"))
#using If condition here.,
if (n1<=n2 and n1<=n3):
    print(n1,"is the smallest num")
elif(n2<=n1 and n2<=n3):
    print(n2, "is the smallest num")
else:
    print(n3,"is the smallest num")