# Author: Dhruv
# USER TO GENERATE ANY RANDOM NUMBER
import random
n = random.randint(1 , 100)

# BEFORE START THE GAME GUESSES STAY ABSULUTE ZERO(0)
guesses = 0

# FALSE BECAUSE USER NOT START GAME YET
won = False

# AFTER NUMBER GUESSED WHENE YOU RUN THE PROGRAM THAT NUMBER GOES INSIDE THE LOOP

# FORM HERE THE LOOP STATS SINCE WE DONT WANT ANY VALUE IN N WE SKIP USING _
for _ in range (1 , 1001):

# NOW WE ENTER A NUMBER
    a = int(input("Guess a number :"))

# IF THE GUEESED NUMBER IS OUTSIDE THE RANGE OF N LOOP DONT COUNT AS A GUESS ASN CONTINUE TO NEXT ITTERATION
    if a < 1 or a > 100:
        print("Please enter a number between 1 and 100")
        continue

# IF THE GUESSED NUMBER IS INSIDE THE RANGE OF N GUESS WILL INCRESS BY 1
    guesses += 1       

# IF THE INTERED NUMBER BY USER IS == RANDOM GENERATE NUMBER THE LOOP BREAKS WITH TOTOAL COUNTS 
    if (a == n):
        won = True
        print("correct!")
        break

# IF THE GUESSED NUMBER IS HIGER THEN N (let's say 67[which alredy inside the loop, not change able before game over])
# ASK USER AGAIN FOR LOWER NUMBER

    elif (a > n):
        print("Lower number please")

# IF THE GUESSED NUMER IS LOWER THEN N (lets's say 67 [which already inside the loop , not chagne able before game over])
# ASK USER AGAIN FOR BIGGER NUMBER
    else:
        print("Higher number please")

# IF THE USER MATCH THE a == n CONDITION THEN LOOP BREAK AND COUNT TOTAL GUESSES AND PRINTS THEM
# IF THE USER NOT MATCH THE a == n CONDITION THEN LOOP CONTINUE for 100 times (use cna increse the size of the loop) YOU COUNT PERFET GUESS
if won:
    print(f"You have guessed the number correctly in {guesses} attempts")
else:
    print("You ran out of attempts. The number was:", n)
    

''' WHILE IS NOT RECOMMENTED RN'''

# import random
# n = random.randint(1 , 100)
# a = -1
# guesses = 1
# while (a != n):
#     a = int(input("Guess the number :"))
#     if (a> n):
#         print("Lower plese")
#         guesses += 1
#     elif (a < n):
#         print("Higger plese :")
#         guesses += 1