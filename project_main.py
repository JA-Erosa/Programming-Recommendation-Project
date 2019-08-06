import obtaining_data as od

flag=True
while flag==True:
    option=int(input("\nWhat would you like to do? (Please type the number)\n"
            "1. Show similar users based on user number\n2. Show movie recommendations based on user number\n"
            "3. Show movie recommendations based on movie id\n4. Show similar users based on movie id\n"
            "5. Exit the program\n"))
    if option==1:
        username=int(input("Please enter your user number (1-610)\n"))
        od.Create_User_Recom(username)
    elif option==2:
        username=int(input("Please enter your user number (1-610)\n"))
        od.Create_Movie_Recom(username)
    elif option==3:
        movieid=int(input("Please enter the movieid \n"))
        od.Movie_Recom_by_Movie(movieid)
    elif option==4:
        movieid=int(input("Please enter the movieid \n"))
        od.User_Recom_by_Movie(movieid)
    elif option==5:
        print("Goodbye!")
        flag=False
    else:
        print("Not a valid option, try again!")
