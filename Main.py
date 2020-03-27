import random
num=random.randint(1,100)
counts=0
guess=0
allguess=[0]
while True:
    guess=0
    guess=int(input('Enter a number:'))
    counts+=1
    allguess.append(guess)
    if guess<=100 and guess>=1:
        if num-guess==0:
            print('The guessed number is correct ')
            print(f'it took you {counts} attempts to guess the correct number' )
            break  
        elif abs(num-guess)<=10:
            if abs(num-guess)<abs(num-allguess[-2]):
                print('warmer')
            else:
                print('warm')
        elif abs(num-guess)>10:
            if abs(num-guess)>abs(num-allguess[-2]):
                print('colder')
            else:
                print('cold')         
    else:
        print('out of bounds')


