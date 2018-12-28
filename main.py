
def compGuess(number):
    import math

    numTries = int(math.log(100,2))
    high = 100
    low = 0
    start = 50

    for x in range(0,numTries+1):
        print(start)
        yes = input("is this your number? (yes,no)")
        if(yes =="yes"):
            print("yay!")
            return
        else:
            hOrL = input("is it higher(H) or lower(L) than the number")

            if(hOrL == "H"):
                low = start
            else:
                high = start

            start = int((high+low)/2)
            print("test")





number = int(input("Please enter a number between 1 and 100 "))
compGuess(number)