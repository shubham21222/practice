i=int(input("enter fact"))
fact=0
if i==0 or i==1:
    print("{}is factorial of {}", format(fact,i))
else:
    for j in range (1,i+1):
        fact=fact*j
        print("{}is factorial of {}".format(fact,i))    