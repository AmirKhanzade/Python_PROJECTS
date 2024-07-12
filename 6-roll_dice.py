import random #for genrating random numbers
def roll_dice(amount:int=2)->list[int]: #this function has one arg named amount which the default value is 2 and must be integer
    if amount<=0:
        raise ValueError #amount of how many to roll dice can not be zero or less than
    
    rolls:list[int]=[] #rolls is list that contains only integer
    for i in range(amount):#amount is the number of how many dice should roll
        random_rolls=random.randint(1,6)#for every number of amount,there will be an random number between 1 to 6
        rolls.append(random_rolls)#these number will go to the rolls list
    sum_list=0
    for item in rolls:
        sum_list+=item  #sum of all numbers in rolls list
    return rolls,sum_list
 
def main():
    while True:#we should be in an infinite loop cause we want to user gives us input as many as he wants
        try:
            user_input:str=input('How many times do you want to roll the Dice? ')
            if user_input.lower()=="exit":
                print('Thanks for playing!')
                break #if user just wanted to get out of the game
            
            print(*roll_dice(int(user_input)),sep=' ,')#int(user_input) will be the amount but if the dont enter it will be 2 by default
            #* front the name of function will unpack items from the list
        except ValueError:
            print('Please enter a valid number ')
            
if __name__=='__main__':
    main()
    
                