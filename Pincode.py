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

  if len(number_two) != len(number):
    print("Your input is too long or too short.")
    quesses = quesses - 1
    continue

  check = ["F"] * 4
  digits = [number.count(str(i)) for i in range(10)]
  count_digits = [i for i in digits]

  if number_two == number and quesses > 1:
    print("Oof! You've beaten me in " + str(quesses) +" turns!")
    break
  else:
   for i, digit in enumerate(number_two):
     index = int(digit)
  if count_digits[index] > 0 and number_two[i] == digit:
   count_digits[index] -= 1
   check[i] = 'G'
  elif count_digits[index] > 0:
   count_digits[index] -= 1
   check[i] = 'C'

  

  e1 = "1980"

  if number_two != number and number_two== e1:
  
     if number_two == e1:
        print ("Yeah! You found an easteregg: The birthyear of LGG!")
     guessesTaken = guessesTaken - 1
  else:
     print(*check, sep=" ")
     print ("Wrong code")

