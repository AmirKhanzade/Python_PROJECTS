#let's create an Aircraft Management system using Python
#Creating an Aircraft object with methodes
class Aircraft :
    
    
    def __init__(self,registration,model,capacity):
        self.registration=registration
        self.model=model
        self.capacity=capacity
        
    def __str__(self):
        return f"Registration : {self.registration}, Model : {self.model}, capacity : {self.capacity}"
    
class Aircraftmanagementsystem :  #create an aircraft management system object with methodes
    def __init__(self):
        self.aircrafts=[] #create a empty list to store aircrafts in it
        
    def add_aircrafts(self):  #defining a method to add aircraft
        registration=input('Enter aircraft registration : ')
        model=input('Enter aircraft model : ')
        capacity=int(input('Enter aircrafts capacity : '))
        aircraft=Aircraft(registration,model,capacity) #create a variable that contains attributes of aircraft object
        self.aircrafts.append(aircraft) #we add item/variable line  above  into our firstcreated empty lists
        print('Aircraft added successfully')
        
    def list_aircraft(self):
        if not self.aircrafts :
            print('NO aircraft available')
            
        else :
            for aircraft in self.aircrafts :
                print(aircraft)  
                          
    def search_aircrafts(self):
        registration=input('Enter your Registration please : ')
        for aircraft in self.aircrafts:
            if aircraft.registration == registration :
                print(aircraft) #print the aircraft from the list
                return
            
        print('Aircraft not found 0_0 ')
        
    def remove_aircraft(self):
        registration=input('please enter aircraft registration to remove : ')
        for aircraft in self.aircrafts:
            if aircraft.registration==registration:
                self.aircrafts.remove(aircraft) #remove aircraft from the list
                print('Aircraft removed successfully')
                return
        print('Aircraft not found here 0_0')
        
    def run(self):
        while True:
            print('\nAircraft Management System')
            print('1.add an aircraft')
            print('2.list aircraft')
            print('3.search aircraft')
            print('4.remove aircraft')
            print('5.exit')
        
            choice=input('Pease enter what you want to do ? : ')    
            if choice == '1':
                self.add_aircrafts() #calling a methode inside an object
            elif choice=='2':
                self.list_aircraft()
            elif choice=='3':
                self.search_aircrafts()
            elif choice=='4':
             self.remove_aircraft()
            elif choice == '5':
                print('Exiting the system...')
                break #breaking the while loop
            else :
                print('Imvalid choice , please try again')
                
if __name__=='__main__':  #coding to run 
    system=Aircraftmanagementsystem()
    system.run()