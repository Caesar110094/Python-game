import random
pincode = ["1221", "9997", "8829", "6765", "9114", "5673", "0103", "4370", "8301", "1022"]
number = (random.choice (pincode))
print(number)
quesses = str(number)
easter = ["1980"]

number_two = (input("Guess the random 4 digit number: "))

quesses = 0
while quesses < 5:
    quesses +=1
    print ("this is your %s guess" %(number_two))
    if number_two < number:
        print ("guess is low")
        break
    elif number_two > number:
        print ("guess is high") 
        break
    elif number_two == number:
        guesses = str(guesses)
        print ("You guess it in : ", guesses + " guesses")
        break
    elif number_two == easter:
        print ("Yeah!")


    

number = str(number)
number_two = str(number_two)
if number == number_two:
  print("correct")
else:
  if number[0] == number_two[0]: 
    print("You got a digit correct") 
  if number[1] == number_two[1]: 
    print("You got a digit correct") 
  if number[2] == number_two[2]: 
    print("You a digit correct") 
  if number[3] == number_two[3]: 
    print("You got a digit correct") 
