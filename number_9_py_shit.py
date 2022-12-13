try:
    wants_to_do = 'Y'
    while(wants_to_do == 'Y'):
        User_value = int(input("Please enter a numerical value: "))
        if((User_value <= 0) and (User_value%8==0)):
            print("Bingo")
        else:
            print("dud...")
        wants_to_do = str(input('Would you like to go again? enter "Y" or "N" to go again: '))
        
except:
       print("The Vlaue you have entered is incorrect please restart the program")