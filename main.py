# Importing Modules And Performing Basic Operations
import mysql.connector as ms
mycon = ms.connect(host="localhost", user="root", passwd="root")
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS STOCKS;")
mycur.execute("USE CRYPTO;")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS USERS (CRPNO INTEGER PRIMARY KEY, ACCNO INTEGER NOT NULL, BANKNAME VARCHAR(90) NOT NULL, PINNO INTEGER NOT NULL, NAME VARCHAR(90) NOT NULL, USERNAME VARCHAR(90) NOT NULL, PASSWD VARCHAR(90) NOT NULL, BALANCE INTEGER NOT NULL);")

# Printing of menu

print("\n\n\n")
print("******************************************************")
print("         -------------------------------------        ")
print("                 Welcome To Stock Arena               ")
print("               Your Turn To Become Richer             ")
print("         -------------------------------------        ")
print("******************************************************")


def display():
    print("\n\n\n")
    print("                          Main Menu                   ")
    print("                     1.Existing User? Login           ")
    print("                     2.New User? Sign Up              ")
    print("                     3.Add New Stock                  ")
    print("                     4.Remove Existing Stock          ")
    print("                     5.Contact Us                     ")
    print("                     6.Exit                           ")
    print("\n\n\n")


# Main Code Starts From Here
# Selection Of Option from Menu
display()
selection = int(input("Please enter a menu option:"))

# Main Loop
while True:
    if selection == 1:
        pass
    elif selection == 2:
        print("Please enter the following details:-")

        # Name
        name = input("Please Enter Your Name: ")
        while name.isalpha() == False:
            name = input("Please Enter Your Real Name: ")

        # Username
        username = input("Please Enter A Username: ")
        mycur.execute("SELECT USERNAME FROM USERS;")
        users = mycur.fetchall()
        print(users)

        # Checking if Username already exists
        while username.lower() in users:
            print("This username has already been taken.")
            username = input("Please Enter Another Username:")

        # Password
        pwd = input("Please Enter A Password:")
        pwd1 = input("Please Enter The Password Again:")

        # Checking if the Passwords match
        while pwd != pwd1:
            print("Both The Passwords Do Not Match")
            pwd = input("Please Enter A Password:")
            pwd1 = input("Please Enter The Password Again:")
        else:
            print("Your Password has been set successfully!")

        # Bank Details + Connection
        bankname = input("Please Enter Your Bank Name:")

        # Checking for 'Bank' at the end
        banktest = bankname.split()
        if banktest[-1].lower() == "bank":
            del banktest[-1]
            "".join(banktest)
        bankname = banktest

        # Process
        accno = input("Please enter your 10-digit account number:")

        # Validating Account number
        while accno.isnumeric() == False or len(accno) != 10:
            print("You've entered an incorrent account number.")
            accno = input("Please enter a valid account number:")

        print("Connecting...")
        pin = int(input("Please Enter Your Pin No:"))

        # Validating PIN number
        while len(str(pin)) != 4:
            print("Please Enter A Valid PIN")
            pin = int(input("Please Enter Your PIN No:"))
        else:
            print(
                f"You've successfully connected to your account {accno}, of {bankname[0]} bank!")

    elif selection == 3:
        pass
    elif selection == 4:
        pass
    elif selection == 5:
        print("For customer support please email us at: support@stockarena.com")
        print("Or call us on our toll free number: 1800-100-200               ")
    elif selection == 6:
        break
    else:
        selection = int(input("Please Enter A Valid Menu Option:"))

    display()
    selection = int(input("Please enter a menu option:"))

print("You've Exited The Program Successfully! Thank you for using Stock Arena!")
