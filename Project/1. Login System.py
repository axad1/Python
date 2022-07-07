while True:
    print("-----\n1. Login\n2. Register\n3. Exit")
    choice = input("Select: ")
    if choice == '1':
        # try if file doesn't exit
        try:
            # open to read
            with open("data.txt", 'r') as file:
                username = input("Enter username: ")
                password = input("Enter password: ")
                # save file data into list
                data = file.readlines()
                # check username
                if username+"\n" in data:
                    # check password
                    if password+"\n" in data:
                        print("Welcome " + username + "!")
                    else:
                        print("password incorrect")
                else:
                    print("False Login!")
        # catch exception
        except(FileNotFoundError):
            print("File error")
            continue

    elif choice == '2':
        # create file if not exist
        file = open("data.txt", 'a')
        file.close()
        # open to read
        file = open("data.txt", 'r')
        data = file.readlines()
        username = input("Enter username: ")
        # check user
        if username+"\n" in data:
            print("User already exist")
            file.close()
            continue

        file.close()
        password = input("Enter password: ")
        # open to write
        file = open("data.txt", "a")
        file.write(username+"\n")
        file.write(password+"\n")
        file.close()
        print("User Registered Successfully")

    elif choice == '3':
        break
    else:
        print("wrong input")