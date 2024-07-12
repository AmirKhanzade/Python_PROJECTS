from random import choice #choice will choose random things from some things

def choose_word():#function to choose a random worde from some words in a list
    word:str=choice(['water','camera','poolparty','swiper'])#we use choice here for choosing random word from the list
    
    user_name:str=input('What is your name ? >> ')#give us user his/her name
    print(f'Welcome to HangMan ,{user_name} ')
    
    #setup the game
    guessed:str='' #keep track of the guessed word by user
    tries:int=3 #only 3 times user can guess    
    
    while tries>0 :
        blanks:int=0 #blanks space of the word/keeping track of them
        
        print('word : ',end=" ")
        
        for character in word :
            if character in guessed: #if the letter that user guessed was correct print the letter
                print(character,end=' ')
            else :
                print('_',end='')
                blanks+=1 #want to make sure there is no blank space if the user guessed all the word
                
        print()#provide blank line
        if blanks==0:
            print('you got it !')
            break #end of the game if there was no blank space
        
        guess:str=input('enter the letter : ')
        if guess in guessed:
            print(f'you already guessed the {guess},please try another letter')
            continue
        
        guessed+=guess #the guessed letter of the user will be in the guessed and will be check by word
        
        if guess not in word:
            tries-=1
            print(f"sorry you have guessed the wrong letter ,{tries} remaining!")
        if tries==0:
            print('sorry you lose the game')
            break
        
if __name__=='__main__':
    choose_word()
    
