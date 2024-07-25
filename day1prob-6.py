''' take a input from the user check if it is positive and even print if it is '''   
num=int(input())
a=int(input())
if(num%2==0):
    if(num>=0):
        print("even positive number")
    else:
        print("even negative number")
else:
    if(a>=0):
        print("odd positive number")
    else:
        print("odd negative number")