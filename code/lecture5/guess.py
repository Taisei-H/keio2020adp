def main():
   import random
   number = random.randint(1, 25)
   running = True

   while running:
       guess = int(input('Enter an integer : '))

       if guess == number:
           print('Congratulations, you guessed it.')
           # this causes the while loop to stop
           running = False
       elif guess < number:
           print('No, it is a little higher than that.')
       else:
           print('No, it is a little lower than that.')
   else:
       print('The while loop is over.')
       # clean-up code usually goes here

   print('Done')

if __name__ == '__main__':
    main()
