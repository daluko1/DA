#dictionary containing current usernames and passwords

users = {"Daniel":"ezpass","cash":"money","Miami":"Heat"}

#validateUser function to allow user to input valid username and password
def validateUser():
        username = input("Enter username:")
        password = input("Enter password:")
#if username and password match, user will be authenticated
        if users[username] == password:
            print("You have been authenticated.")
        else :
#or else user will have failed authentication and be prompted to make a selection again
            print("You have failed authentication")
        return False

#changePw function allows user to change password
def changePw():
        username = input("Enter username:")
        password = input("Enter password:")
#if validated, user will be able to enter a new password
        if users[username] == password:
            newPass = input("Enter new password:")
            users[username] = newPass
        return users

print("1. Authenticate\n2. Reset Password\n3. Log Off")
userChoice = int(input("Which would you like to do?:"))
#while loop allowing user to choose between authenticating, changing password, or logging off
while userChoice!=3:
    if userChoice == 1:
        validateUser()
    elif userChoice== 2:
        users = changePw()
    print("1. Authenticate\n2. Reset Password\n3. Log Off")
    userChoice = int(input("Which would you like to do?:"))
print("Goodbye, thank you for logging off!")
