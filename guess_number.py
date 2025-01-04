import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print(f"Guess a number between 1 and {x}.")

    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')
        except ValueError:
            print("Please enter a valid number.")
    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


def computer_guess(x):
   low=1
   high=x
   feedback= ''
   while feedback!='c':
       if low!=high:
         guess =random.randint(low,high)
       else:
         guess=low
       feedback =input(f'Is {guess} too high(H) ,too low(L) or correct(C)??').lower()
       if feedback =='h':
           high=guess-1
       if feedback =='l':
          low=guess+1

   print('yay!computer guessed,{guess} ')
  
computer_guess(1000)