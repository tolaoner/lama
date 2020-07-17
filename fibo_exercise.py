##fibonacci generator
import random
def fibonacci_generator():
    no_numbers=int(input('Please enter the no. numbers you want to get from Fibonacci series: '))
    fibonacci_list=[]
    fibonacci_list.append(1)
    fibonacci_list.append(1)
    for i in range(2,no_numbers):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
    print(fibonacci_list)
    #for element in fibonacci_list:
#fibonacci_generator()
def guess_game():
    guess_bool=True
    i=0
    the_number = random.randint(1, 10)
    while guess_bool:
        inp1=input('Guess a number between 0,10: ')
        if inp1 == 'exit':
            print(f'Guess trials: {i}')
            break
        decision=int(inp1)
        if decision==the_number:
            guess_bool=False
            i += 1
            print(f'Congrats you found it! \n Guess trials: {i}')
        else:
            guess_bool=True
            difference=abs(the_number-decision)
            if difference>=5:
                print('Too far!')
            else:
                print('Close!')
            i += 1
guess_game()





