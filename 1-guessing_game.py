from random import randint #random integer
lower_number=1
higher_number=10
random_number:int=randint(lower_number,higher_number)#random number will be an integer between 1 - 10
print(f"guess the number in the range between {lower_number} and {higher_number}  ")
#create an infinite loop
while True:
    try:
        user_input:int=int(input('guess : ')) #user input must be an integer
    except ValueError:
        print('please enter valid number')
        continue # while we got there , the loop must start again based user input
        
    if user_input>random_number:
        print('the number is lower')
    elif user_input<random_number:
        print("the number is higher")
    else :
        print('wow!you guessed it right ^_^ ')
        break
#by creating this loop when the user have entered a wrong number or wrong format
#he has to enter his input again and our programm will not be stopped !!
