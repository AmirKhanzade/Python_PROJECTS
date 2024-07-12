import random
import sys

class rock_paper_scissors: #crate class wich has methodes
    def __init__(self):
        print('welcome to the game!!!')
        self.moves:dict={'rock':' hard as rock','paper':'clean as paper','scissors':'sharp as sciossors'} #creating moves
        self.valid_moves:list[str]=list(self.moves.keys()) #only valid moves are words equal to self.move keys of this dictionary
    def main_game(self):
        user_move:str=input('Rock,paper or scissors ? >> ').lower() #turn user input into lower case
        if user_move=='exit':
            print('thanks for playing !')
            sys.exit()#exit the game and system
        if user_move not in self.valid_moves :
            print('please enter valid moves')
            return self.main_game() #return the method to play the game from the beginning in order to user enter valid move
        ai_move:str=random.choice(self.valid_moves)#ai will choose from the valid moves list , valid moves contains keys of  dict moves
        
        self.display_game(ai_move,user_move)#after the main game we have to display the moves
        self.check_moves(ai_move,user_move)#then we have to check the moves
            
            
            
    def display_game(self,ai_move:str,user_move:str):
        print('-----------')#divider
        
        print(f'you choose {self.moves[user_move]}')#accessing the values of moves dictionary by the keys,user input will be the same as keys of dict
        print(f'ai choose {self.moves[ai_move]}')
        print('--------') #more divider
        
    def check_moves(self,ai_move:str,user_move:str):
        if user_move=='rock' and ai_move=='rock':
            print('you just tie')
            return self.display_game
        if user_move=='rock' and ai_move=='paper':
            print('ai won!try again')
            return self.display_game(ai_move,user_move)
        if user_move=='rock' and ai_move=='scissors':
            print('you won over the ai,wanna try again?')
            return self.display_game(ai_move,user_move)
        if user_move=='paper' and ai_move=='paper':
            print('you both tied^_^')
            return self.display_game(ai_move,user_move)
        if user_move=='paper' and ai_move=='rock':
            print('you won the ai !')
            return self.display_game(ai_move,user_move)
        if user_move=='paper' and ai_move=='scissors':
            print('ai beat you !')
            return self.display_game(ai_move,user_move)
        if user_move=='sciossers' and ai_move=='rock':
            print('ai beat you !')
            return self.display_game(ai_move,user_move)
        if user_move=='scissors' and ai_move=='paper':
            print('you won the ai !')
            return self.display_game(ai_move,user_move)
        if user_move=='scissors' and ai_move=='scissors':
            print('you both just tied !')
            return self.display_game(ai_move,user_move)
        
if __name__=='__main__':
    rps=rock_paper_scissors()
    
    while True:
        rps.main_game()
        
        
        
        
        
    