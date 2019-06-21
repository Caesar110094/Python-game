import random
pincode = ["1221", "9997", "8829", "6765", "9114", "5673", "0103", "4370", "8301", "1022"]
number = (random.choice (pincode))
print(number)


number_two = (input("Guess the random 4 digit number: "))

quesses = 0
while quesses < 10:
    quesses +=1    
    print ("This is your guess: %s" %(number_two))
    if number_two == number:
        quesses = str(quesses)
        print ("You guess it in : ", quesses + " guesses")
    break

number = str(number)
number_two = str(number_two)
if number == number_two:
  print("You guessed it!")
else:
  if number[0] == number_two[0]: 
    print("G")  
  if number[1] == number_two[1]: 
    print("G") 
  if number[2] == number_two[2]: 
    print("G")
  if number[3] == number_two[3]: 
    print("G")
  
  if number[0] != number_two[0]: 
    print("F") 
  if number[1] != number_two[1]: 
    print("F") 
  if number[2] != number_two[2]: 
    print("F") 
  if number[3] != number_two[3]: 
    print("F") 
  if number != number_two:
    print ("Wrong Code")
    

