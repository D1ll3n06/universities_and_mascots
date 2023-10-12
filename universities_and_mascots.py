# Dillen Dela Cruz
# 12/6/2022


#main function
def main():
    
    #start up banner
    print()
    print('-----------------------------------------------')
    print('Welcome to the Universities and Mascots program')
    print('-----------------------------------------------')
    
    #dictionary of Universities and their Mascots
    school = {"UTSA":"Roadrunners","UT":"longhorns","UTRGV":"Vaqueros",
          "Texas A&M International":"Dustdevil","Texas Tech":"Red Raiders",
          "Baylor":"Bears","Texas Chritian":"Horned Frog",
          "Sam Houston State":"Bearcats","Teaxas State":"Bobcats",
          "Rice":"Owls",}
    
    #Priming the loop to begin
    Repeat = "Y"
  
    # Loop initialized and program starts
    while Repeat == "Y":
    # if and elif statements that call the appropriate action when prompted by the user   
       choice = get_menu()
   
       if choice == 1:
           print("")
           view(school)
       
       elif choice == 2:
           print("")
           viewMascot(school)
   
       elif choice == 3:
           print("")
           viewSchool(school)
       
       elif choice == 4:
           print("")
           numberItems(school)
           
       elif choice == 5:
          print("")
          lookUpSchool(school)
   
       elif choice == 6:
           print("")
           lookUpMascot(school)
       
       elif choice == 7:
           print("")
           sortMascot(school)
           
       elif choice == 8:
           print("")
           sortSchool(school)
   
       elif choice == 9:
           print("")
           add(school)
       
       elif choice == 10:
           print("")
           remove(school) 
    
       elif choice == 11:
           print("")
           change(school)
    
       elif choice == 12:
            print("")
            wipe(school)
        
       elif choice == 13:
           print("")
           print('you chose to exit menu. goodbye')
           Repeat = "no" 
   
# options availble for user input
def get_menu():
    print("")
    print("Select an option")
    print("---------------------------")
    print("1. Display all the Universities and their Mascots")
    print("2. Display all the Mascots in the dictionary")
    print("3. Display all the Universities in the dictionary")
    print("4. Display how many Universities/Mascot pairs exists in the dictionary")
    print("5. Look up a specific University in the dictionary")
    print("6. Look up a specific Mascot in the dictionary")
    print("7. Divide the Mascots A-M then M-Z")
    print("8. Divide the University A-M then M-Z")
    print("9. Add a University and its Mascot to the dictionary")
    print("10. Remove a University and its Mascot from the dictionary")
    print("11. Change a Universities Mascot")
    print("12. Remove all Universities and Mascots from the Universities options")
    print("13. Exit the program menu")
    print("")
    
    choice = int(input("Enter your choice: "))
# while loop that runs users through the available selections
    while choice < 1 or choice > 13:
        choice = int(input("Enter a valid choice: "))
    
    return choice    

#for loop used to return keys (Universities) and values (Mascots) in the dictionary
def view(school):
    print(f'{"Name of University:": <29}{"Mascots:": ^12}')
    print("----------------------------------------")
    
    for k in sorted(school):
        print(f'{k : <30} {school[k]}')
    
    
# for statement used to locate a value (Mascot)
def viewMascot(school):
    print(f'{"Mascots": ^31}')
    print("-------------------------------")
    for v in sorted(school.values()): #uses the .values method to retrive the values 
        print(f'*** {v: ^23}{"***": ^6}')
  
# for statement used to locate a key (Universities)
def viewSchool(school):
    print(f'{"Name of Universities": ^31}')
    print("-------------------------------")
    for k in sorted(school.keys()): #uses the .keys method to retrieve the keys
        print(f'*** {k: ^23}{"***": ^6}')
        
        
# len function used to obtain the number of elements in the dictionary    
def numberItems(school):
    print("")
    numberItems = len(school)
    print("There are" , numberItems , "University/Mascot pairs.")


# if else statement used to locate a key (University)
def lookUpSchool(school):
    name = input("Enter a University you would like to find: ")
    if name in school.keys(): #determines if name is located in the keys of the dictionary
        print("")
        print("We were able to find the university,",name,",in the dictionary.")
    else: #if name is not found else statement will run and print out statement
        print("")
        print(name, "was not found in the dictionary.")


# if else statement used to locate a value (Mascot)
def lookUpMascot(school):
    name = input("Enter a Mascot you would like to find: ")
    
    if name in school.values(): #determines if name is located in the values of the dictionary
        print("")
        print("We were able to find the mascot,",name, ",in the dictionary.")
    else: #if name is not found else statement will run and print out statement
        print("")
        print(name, "was not found in the dictionary.")


#sorts the values (mascot) from A-M then N-Z
def sortMascot(school):
    list2 = list(school.values()) #turns the dictionary into a list 


    list2.sort() #sorts list in ascending order 
    i = 0 
    n = 0

    print(f'{"Mascots: A-M": ^27}')
    print("--------------------------")
    while i < len(list2):  
        if list2[i].startswith(('A','B','C','D','E','F','G','H','I','J','K','L','M')) : #uses the startwith method to get the mascots that start with A-M
            print(f'***{list2[i]: ^20}***') 
        i+=1 

    print("")

    print(f'{"Mascots: N-Z": ^27}')
    print("--------------------------")
    while n < len(list2): #loop used to get through the entire list 
        if list2[n].startswith(('N','O','P','Q','R','S','T','U','V','W','X','Y','Z')) : #uses the startwith method to get the mascots that start with N-Z
            print(f'***{list2[n]: ^20}***')
        n+=1


#sorts the keys (universities) from A-M then N-Z
def sortSchool (school):
    list1 = list(school.keys()) #turns the dictionary into a list


    list1.sort() #sorts list in ascending order 
    i = 0 
    n = 0

    print(f'{"Universities: A-M": ^34}')
    print("---------------------------------")
    while i < len(list1):  
        if list1[i].startswith(('A','B','C','D','E','F','G','H','I','J','K','L','M')) : #uses the startwith method to get the universities that start with A-M
            print(f'***{list1[i]: ^26}{"***": ^5}') 
        i+=1 

    print("")
 
    print(f'{"Universities: N-Z": ^34}')
    print("---------------------------------")
    while n < len(list1): #loop used to get through the entire list 
        if list1[n].startswith(('N','O','P','Q','R','S','T','U','V','W','X','Y','Z')) : #uses the startwith method to get the universities that start with N-Z
            print(f'***{list1[n]: ^27}{"***": ^1}')
        n+=1

# if else statments used to add Collection Items and Prices to dictionary    
def add(school):  

    name= input("Enter the name of the University you want to add: ") #user will input new key
    mascot = input("Enter the name of " + name + "'s mascot: ") #user will input new value for the key

    if name not in school:
        confirm = input("Enter Yes to Confirm your addition of " + name + ' and its mascot, ' + mascot+": ")

# if else statements used to confirm users selection before adding to dictionary        
        if confirm in ["Yes" , "yes"]:
            school[name] = mascot # puts together user's input of the new key and value and adds it to the dictionary
            print("")
            print("Your addition of " + name + ' and its mascot, ' + mascot + " has been added to the dictionary.")
            print(view(school)) #gets the view function to print out dictionary with the new keys and values
        else:
            print("")
            print("You have chose not to make an addition at this time.")
    else:
        print("")
        print(name + " and its mascot, " + mascot + ", already exist in the dictionary.")
        
        
# if else statements used to remove a key (University) and value (Mascot) from the dictionary        
def remove(school):
    name = input("Enter a University to remove: ")

    if name in school:
# if else statements used to confirm users selection
        confirm = input("Are you sure you would like to remove " + name +" and its mascot, " + school[name] + "? ")
        
        if confirm in ["Yes" , "yes"]:
            print("")
            print(name,"and its mascot,",school[name],",have been removed from the dictionary.")
            del school[name] #del method to delete the university the user input
            print("")
            print(view(school))
        else: #else statement will run if user does not input yes or Yes
            print("")
            print("You have chosen not to remove " + name + " and its mascot, " + school[name] + ".")
            
    else: #else statement will run if user inputs a university that does not exist in the dictionary
        print("")
        print(name, "and its mascot was not found.")




# if else statements used to change the value (Mascot) of a key (university) in the dictionary
def change(school):
    name = input("Enter the University that you would like to change the mascot: ")

    if name in school:
        mascot = input("Enter the new mascot for " + name +": ") #user input to change value
        
        confirm = input("Enter Yes to Confirm the change in mascot for " + name +": ")
        
    # if else statements used to confirm users selection before changing the value (mascot)
        if confirm in ["Yes" , "yes"]:

            school[name] = mascot #changes the value of the key that the user input
            print("")
            print("The", name, "mascot has been changed to", school[name])
            print("")
            print(view(school)) #uses the view function to print out the list with the changes value (mascot)
        else: # else statment will run if user does not input yes or Yes
            print("")
            print("You have chosen not to change " + name +"'s mascot to the " + mascot +"." )
            
    else: #else statement will run if user inputs a university that does not exist in teh dictionary
        print("")
        print(name, "was not found. We could not preform the change.")


# if else statement that deletes every university and mascot from the dictionary
def wipe(school):
    confirm = input("Are you sure you want to remove all Universities and their Mascots from the dictionary?: ")
    
    if confirm in ["Yes" , "yes"]:
        school.clear() #uses clear method to clear directory
        print("")
        print("All the Universities and their Mascots have been removed.")
        print(view(school)) #uses the view function to print the empty dictionary
    else:
        print("")
        print("You have chosen not to remove all Universities and their Mascots.")

# only runs the code inside the if statement when the program is run directly by the Python interpreter
if __name__ == '__main__':
    main()