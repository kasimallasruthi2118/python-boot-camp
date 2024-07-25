''' person x goes to market he will buy 10 apples and two dozen bhananas and next he will buy 8 organges and next the cost of each is 15 rupees and the cost of 1 bhanana is 4 rupess
and the cost of orange is 5 mother of x, i.e gave 700 rupees to mr x and says some amount will be left with you'''
apples=int(input())
bananas =int(input())
oranges=int(input())

total=(15*apples + 4*bananas + 5*oranges)
print(total)
if(total < 700):
    print("shopkepper is not cheater")
else:
    print("the shopkepper is cheater") 