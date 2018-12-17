#!/usr/bin/env perl3
 
#
# Bulls and Cows
#
 
import random
 
digits = [ x for x in range(10) ]
random.shuffle(digits)
conceived = digits[:4]
if conceived[0] == 0 :
    conceived[0] = conceived[1]
    conceived[1] = 0
 
while True:
    guessed = int(input("Number: "))
    if not 999 < guessed < 10000 :
        print("Need number from 1000 to 9999")
        continue
    testing = [ int(x) for x in str(guessed) ]
    if testing == conceived :
        print("Oh yeah! You win!")
        print("It was", conceived)
        break
    for n, d in enumerate(testing) :
        if conceived[n] == d :
            print("B", end="")
        elif d in conceived :
            print("C", end="")
        else :
            print(d, end="")
    print()