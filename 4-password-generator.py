import string #to use special characters
import secrets #to generate really secure random numbers

def contains_upper(password:str)->bool:#to check if just one character of password is upper or not
    for character in password :
        if character.password.isupper():
            return True
        
    return False
def contains_symbol(password:str)->bool:#to check if only one letter of password is symbol or not
    for character in password:
        if character in string.punctuation: #check for symbol and special characters
            return True
    return False

def generate_password(length:int,symbol:bool,uppercase:bool)->str:#geneerate password based on wanting to have symbol
#or uppercase or how many length
    combination:str=string.ascii_lowercase+string.digits #password is combination of leeter and numbers
    if symbol:#if symbol value was true you cann ad symbol to password combination
        combination+=string.punctuation
    if uppercase:#if uppercase value was true you cann ad uppercase to your password combination
        combination+=string.ascii_uppercase
        
    combination_length=len(combination)#the total amount of characters in the string
    new_password:str=''#here we store our new password so it should be empty string
    
    for _ in range(length):
        new_password+=combination[secrets.randbelow(combination_length)]#to genrate random numbers between 1 to combination_length
        
    return new_password

if __name__=='__main__':
    new_pass=generate_password(length=10,symbol=True,uppercase=True)#enter the arguments values and calling the function
    print(new_pass)
    
    
                        
    