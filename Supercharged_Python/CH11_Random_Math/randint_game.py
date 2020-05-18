import random

def play_the_game():
    n = random.randint(1, 50)
    while True:
        guess = int(input('Enter guess:'))
        if guess == n:
            print('Success! You win.')
            break
        elif guess < n:
            print('Too low.', end=' ')
        else:
            print('Too high.', end=' ')

while True:
    play_the_game()
    ans = input('Want to play again? (Y or N): ')
    if not ans or ans[0] in 'Nn':
        break
