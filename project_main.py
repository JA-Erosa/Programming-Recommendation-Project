import obtaining_data as od

username=int(input("Please enter your user number (1-610)\n"))
flag=True
while flag==True:
    option=int(input("\nWhat would you like to do? (Please type the number)\n"
            "1. Show similar users\n2. Show movie recommendations\n3. Switch user number\n4. Exit the program\n"))
    if option==1:
        od.Create_User_Recom(username)
    elif option==2:
        od.Create_Movie_Recom(username)
    elif option==3:
        username=int(input("Please enter your user number (1-610)\n"))
    elif option==4:
        print("Goodbye!")
        flag=False
