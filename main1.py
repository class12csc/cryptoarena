# Importing Modules And Performing Basic Operations
import mysql.connector as ms
mycon = ms.connect(host="localhost", user="root", passwd="root")
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS STOCKS;")
mycur.execute("USE STOCKS;")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS USERS (ACCNO INTEGER NOT NULL, BANKNAME VARCHAR(90) NOT NULL, PINNO INTEGER NOT NULL, NAME VARCHAR(90) NOT NULL, USERNAME VARCHAR(90) NOT NULL, PASSWD VARCHAR(90) NOT NULL, AADHAR VARCHAR(12) PRIMARY KEY, BALANCE VARCHAR(18));")
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

def display_main():
    print("\n\n\n")
    print("                          Main Menu                   ")
    print("                     1.Existing User? Login           ")
    print("                     2.New User? Sign Up              ")
    print("                     3.Exit                           ")
    print("\n\n\n")


def display_submenu():
    print("                        Account Menu                  ")
    print("                     1.Show Balance                   ")
    print("                     2.Deposit Money                  ")
    print("                     3.Withdraw Money                 ")
    print("                     4.Change username                ")
    print("                     5.Show Available Stocks          ")
    print("                     6.Buy New Stock                  ")
    print("                     7.Add New Stock                  ")
    print("                     8.Remove Existing Stock          ")
    print("                     9.Return to Main Menu            ")


# Main Code Starts From Here

# Selection Of Option from Menu
display_main()
selection = int(input("Please enter a menu option:"))


def submenu(user):
    while True:
        """
        1) Show balance
        2) Show available stock
        3) Buy Stock
        4) Add
        5) Remove
        6) Return to Main Menu

        """
        print("\n\n\n")
        display_submenu()
        print("\n\n\n")
        selec = int(input("Please enter a menu option:"))
        print()
        if selec == 1:
            # Diplaying Balance
            mycur.execute(
                "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
            balance_report = mycur.fetchall()
            for i in balance_report:
                print(f"These is your current balance {i[0]}.")

        elif selec == 2:
            deposit = input("Please enter amount of money to be deposited:")

            while deposit.isnumeric() == False:
                print("You've entered an invalid amount.")
                deposit = input("Please enter a valid amount: ")

            mycur.execute(
                "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
            balance_report = mycur.fetchall()
            net_balance = int(balance_report[0]) + int(deposit)
            mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                str(net_balance), user))

        elif selec == 3:
            withdraw = input("Please enter amount of money to be withdrawn:")

            while withdraw.isnumeric() == False:
                print("You've entered an invalid amount.")
                deposit = input("Please enter a valid amount: ")

            mycur.execute(
                "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
            balance_report = mycur.fetchall()
            net_balance = int(balance_report[0]) - int(withdraw)
            mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                str(net_balance), user))

        elif selec == 4:
            pass

        elif selec == 5:
            # Displaying the stocks
            print()
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
                    print()

        elif selec == 6:
            pass

        elif selec == 7:
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

            print(
                f"The {stkname} stock has been successfully added to the market!")

        elif selection == 8:

            # Validating the Stock name
            stkrem = input(
                "Please enter stock to be removed from the listing:")
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

        elif selection == 9:
            print("You've successfully returned to the main menu!")


# Main Loop
while True:
    if selection == 1:
        mycur.execute("SELECT USERNAME FROM USERS;")
        usernames = mycur.fetchall()
        print(usernames)
        usrname_existing = input("Please enter your username:")
        print()
        while (usrname_existing + ",") not in usernames:
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
            print("You've entered an invalid name.")
            name = input("Please enter your real name: ")

        # Username
        username = input("Please enter a username: ")
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

        # Aadhar number
        aadhar = input("Please enter your Aadhar number:")

        while aadhar.isnumeric() == False:
            print("You've entered an invalid Aadhar number.")
            name = input("Please enter a valid Aadhar number: ")

        mycur.execute("SELECT AADHAR FROM USERS;")
        aadhars_of_users = mycur.fetchall()

        # Checking if Aadhar is repeated
        while username.lower() in users:
            print("This Aadhar has already exists.")
            reply = input("Existing User? Y/N?")
            if reply.lower() == "y":
                print("Then please do proceed to the existing user option.")
                print()
                break
            else:
                aadhar = input("Please enter your aadhar number again:")
                print()

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

        # Balance
        balance = input(
            "Please enter amount of money you wish to deposit (in $):")

        while balance.isnumeric() == False:
            print("You've entered an invalid amount.")
            balance = input("Please Enter a valid amount:")

        mycur.execute(
            "INSERT INTO USERS VALUES ('{}','{}','{}','{}', '{}', '{}', '{}', '{}')".format(accno, bankname[0], pin, name, username, pwd, aadhar, balance))
        print()
        print(
            f"You've successfully connected to your account {accno}, of {bankname[0]} bank and deposited ${balance} !")

        submenu(username)

    elif selection == 3:
        break

    else:
        selection = int(input("Please Enter A Valid Menu Option:"))

    display_main()
    selection = int(input("Please enter a menu option:"))

print("You've exited the program successfully! Thank you for using Stock Arena!")
