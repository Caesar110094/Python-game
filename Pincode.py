import random
pincode = ["1221", "9997", "8829", "6765", "9114", "5673", "0103", "4370", "8301", "1022"]
number = (random.choice (pincode))
print(number)


quesses = 0
while quesses < 10:
  number_two = input("Guess the random 4 digit number: ")

  quesses += 1    
  print ("This is your guess: %s" %(number_two))
  if number_two == number:
    quesses = str(quesses)
    print ("You guess it in : ", quesses + " guesses")  

  number = str(number)
  number_two = str(number_two)
  
  for index in range(10):
  if number[index] == number_two[index]: 
    print("G")  
    
  if number[index] != number_two[index]: 
    print("F") 

    print ("Wrong Code")
    

