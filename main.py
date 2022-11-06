# Importing Modules And Performing Basic Operations
import mysql.connector as ms
mycon = ms.connect(host="localhost", user="root", passwd="root")
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS STOCKS;")
mycur.execute("USE STOCKS;")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS USERS (ACCNO INTEGER NOT NULL, BANKNAME VARCHAR(90) NOT NULL, PINNO INTEGER NOT NULL, NAME VARCHAR(90) NOT NULL, USERNAME VARCHAR(90) NOT NULL, PASSWD VARCHAR(90) NOT NULL, AADHAR VARCHAR(12) PRIMARY KEY, BALANCE VARCHAR(18);")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS STOCKS(STKNAME VARCHAR(90) PRIMARY KEY, VALUE CHAR(90) NOT NULL, SYMBOL CHAR(9) NOT NULL);")

# Inserting default Stock values
mycur.execute("INSERT INTO STOCKS VALUES ('Apple','139','AAPL');")
mycur.execute("INSERT INTO STOCKS VALUES ('Saudi Aramco', '9.13', '2222.sr')")
mycur.execute("INSERT INTO STOCKS VALUES ('Microsoft', '221.36', 'MSFT')")
mycur.execute("INSERT INTO STOCKS VALUES ('Google', '86.70', 'GOOG')")
mycur.execute("INSERT INTO STOCKS VALUES ('Amazon', '90.98', 'AMZN')")
mycur.execute("INSERT INTO STOCKS VALUES ('Tesla', '207.47', 'TSLA')")
mycur.execute("INSERT INTO STOCKS VALUES ('Berkshire Hathway', '287', 'BRK')")
mycur.execute("INSERT INTO STOCKS VALUES ('Unitded Health', '538.71', 'UNH')")
mycur.execute("INSERT INTO STOCKS VALUES ('Exxon Mobil', '112.31', 'XOM')")
mycur.execute("INSERT INTO STOCKS VALUES ('Johnson', '171.48', 'JNJ')")
mycur.execute("INSERT INTO STOCKS VALUES ('Visa', '196.98', 'V')")
mycur.execute("INSERT INTO STOCKS VALUES ('JPMorgan', '130.58', 'JPM')")
mycur.execute("INSERT INTO STOCKS VALUES ('Walmart', '140.97', 'WMT')")
mycur.execute("INSERT INTO STOCKS VALUES ('Nvidia', '141.56', 'NVDA')")
mycur.execute("INSERT INTO STOCKS VALUES ('Chevron', '183.42', 'CVX')")
mycur.execute("INSERT INTO STOCKS VALUES ('Eli Lilly', '357.41', 'LLY')")
mycur.execute("INSERT INTO STOCKS VALUES ('LVMH', '663.61', 'MCPA')")
mycur.execute("INSERT INTO STOCKS VALUES ('TSCM', '62.48', 'TSM')")


# Printing of menu

print("\n\n\n")
print("******************************************************")
print("         -------------------------------------        ")
print("                 Welcome To Stock Arena               ")
print("               Your Turn To Become Richer             ")
print("         -------------------------------------        ")
print("******************************************************")


# Functions used

def display():
    print("\n\n\n")
    print("                          Main Menu                   ")
    print("                     1.Existing User? Login           ")
    print("                     2.New User? Sign Up              ")
    print("                     3.Add New Stock                  ")
    print("                     4.Remove Existing Stock          ")
    print("                     5.Diplay All The Stocks          ")
    print("                     6.Exit                           ")
    print("\n\n\n")


# Main Code Starts From Here

# Selection Of Option from Menu
display()
selection = int(input("Please enter a menu option:"))

# Main Loop
while True:
    if selection == 1:
        mycur.execute("SELECT USERNAME FROM USERS;")
        usernames = mycur.fetchall()
        usrname_existing = input("Please enter your username:")
        print()
        while usrname_existing not in usernames:
            print("This user doesn't exist!")
            reply = input("New User? Y/N?")
            if reply.lower() == "y":
                print("Then please do proceed to the sign up option.")
                print()
                break
            else:
                usrname_existing = input("Please enter your username again:")
                print()

    elif selection == 2:
        print("Please enter the following details:-")

        # Name
        name = input("Please Enter Your Name: ")
        while name.isalpha() == False:
            print("Please enter a valid name.")
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

        mycur.execute(
            "INSERT INTO USERS VALUES ('{}','{}','{}','{}', '{}', '{}')".format(accno, bankname, pin, name, username, pwd))

    elif selection == 3:

        # Stock name
        stkname = input("Please enter stock name:")
        while stkname.isalpha() == False:
            print("Please enter a valid name.")
            stkname = input("Please enter the real name of the stock: ")

        # Stock value + Checking if the value entered is valid
        stkval = input(
            "Please enter stock value (in $):")

        while True:
            try:
                float(stkval)
                break
            except ValueError:
                print("You've entered an invalid price of the stock.")
                stkval = input(
                    "Please enter a valid price of the stock (in $):")

        # Stock Symbol
        stksym = input("Please enter a 3-letter symbol for the stock:")
        while stksym.isalpha() == False or len(stksym) != 3:
            print("You've entered an invalid symbol.")
            stksym = input(
                "Please enter a valid 3-letter symbol for the stock:")

        print(stkval)

        mycur.execute(
            "INSERT INTO STOCKS VALUES('{0}','{1}','{2}');".format(stkname.capitalize(), stkval, stksym.upper()))
        # mycon.commit()

        print(f"The {stkname} stock has been successfully added to the market!")

    elif selection == 4:

        # Validating the Stock name
        stkrem = input("Please enter stock to be removed from the listing:")
        while stkrem.isalpha() == False:
            print("Please enter a valid name.")
            stkname = input("Please enter the real name of the stock: ")
        mycur.execute(
            "SELECT * FROM STOCKS WHERE STKNAME = '{}'".format(stkrem.capitalize()))
        stkrec = mycur.fetchall()

        # Checking and Deleting The Stock
        if len(stkrec) == 0:
            print("No such stock exists.")

        else:
            mycur.execute(
                "DELETE FROM STOCKS WHERE STKNAME = '{}'".format(stkrem))
            print(
                f"The {stkrem} has been successfully removed from the listing!")

    elif selection == 5:
        # Displaying the stocks
        mycur.execute("SELECT * FROM STOCKS;")
        displayingstks = mycur.fetchall()
        if len(displayingstks) == 0:
            print("No stocks have been added yet")
        else:
            print("Stock Name                   ",
                  "Stock Value                  ", "Stock Symbol                  ")
            for i in displayingstks:
                for j in i:
                    spaces = 30 - len(j)
                    print(j, end=" " * spaces)

    elif selection == 6:
        break

    else:
        selection = int(input("Please Enter A Valid Menu Option:"))

    display()
    selection = int(input("Please enter a menu option:"))

print("You've exited the program successfully! Thank you for using Stock Arena!")
