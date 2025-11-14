from random import randrange
import os

def main():
    n = ''
    attempt = 0
    while n != 'q':
        print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
\nPlease select the difficulty level:\n1. Easy (7 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")
        num = int(input('Enter your choice: '))
        while True:
            if num == 1:
                attempt = 7
                print('\nGreat! You have selected the Easy difficulty level.')
                break
            elif num == 2:
                attempt = 5
                print('\nGreat! You have selected the Medium difficulty level.')
                break
            elif num == 3:
                attempt = 3
                print('\nGreat! You have selected the Hard difficulty level.')
                break
            else:
                print('Incorrect input')
                num = int(input('Enter your choice:'))
        print("Let's start the game!")
        number = randrange(1, 101)

        num2 = int(input("Enter your guess: "))
        while attempt != -1:
            if num2 == number:
                print(f"Congratulations! You guessed the correct number in {attempt} attempts.\n")
                break
            
            elif num2 > number:
                print(f"Incorrect! The number is less than {num2}.")
                attempt -= 1

            elif num2 < number:
                print(f"Incorrect! The number is greater than {num2}.")
                attempt -= 1

            if attempt > 0:
                num2 = int(input("Enter your guess: "))

        else:
            print(f'You lost, the correct answer was {number}\n')

        n = input('To continue, press Enter or q to exit: ')
        os.system('cls')
        
x = main()
print(x)