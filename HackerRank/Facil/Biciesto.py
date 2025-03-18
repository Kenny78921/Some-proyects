
#% https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

from os import system
system("cls")

def is_leap(year):
    leap = False

    if (year % 4) == 0 and (year % 100) != 0:  
        print("Si es")

    elif (year % 400) == 0 :
        print("Si es")
        
    else:
        print("No es")

    return leap


year = int(input())

is_leap(year)
