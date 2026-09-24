print ('Type Create Account (to create an account)')
print ('Type Log In (to log in)')
Account = input("Create Account Or Log In - ").lower().upper().title()
if Account == ('Create Account'):
    Name = str(input('Enter Name - ')).title()
    Username = input('Username - ')
    print('Date_of_Birth: ')
    Date = (input('Date - '))
    Month = (input('Month - '))
    Year = int(input('Year - '))
    Gender = str(input('Gender - ')).lower().upper().title()
    if Gender == 'Male':
        Email = input('Enter Email address - ').lower()
        Create_Password = input('Create Password - ')
        Password = input('Enter Password - ')
    elif Gender == 'Female':    
        Email = input('Enter Email address - ').lower()
        Create_Password = input('Create Password - ')
        Password = input('Enter Password - ')
    else:
        print('please type your gender')    
    if Password == Create_Password:
        print('------------')
        print('Name - ' + Name)
        print('Username - ' + Username)
        print('Date of Birth - ' + str(Date) + '-' + str(Month) + '-' + str(Year))
        print('Gender - ' + Gender)
        print('Email - ' + Email)
        print('Password - ' + Password)
        print('Your account succesfully created')
    else:
        print('Password Incorrect')
    print('------------')        
    print("want to log in?")  
    Yes_No = str(input('Type Yes or No - ')).lower().upper().title()  
    if Yes_No == 'Yes': 
        Username1 = input('Username - ')
        Password1 = input('Enter Password - ')
        if Username == Username1 and Password == Password1:
            print('Username and Password are correct')
            print('Access Granted')
        else:
            print('Username and Password are Incorrect')
            print('Access Denied')   
    elif Yes_No == 'No': 
        print('Quit') 
    else:
        print('please type Yes or No')               
elif Account == ('Log In'):
    Username = input('Enter Username - ')
    Password = input('Enter Password - ')
    print('Username - ' + Username)
    print('Password - ' + Password)
    if Username == 'user04' and Password == '123abcxyz':
        print('Username and Password are correct')
        print('Access Granted')
    else:
         print('Username and Password are Incorrect')
         print('Access Denied')   
else: 
    print('please enter Create Account or Log In')
    

    
