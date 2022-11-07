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
    print("                     4.Delete Account                 ")
    print("                     5.Show Available Stocks          ")
    print("                     6.Buy New Stock                  ")
    print("                     7.Add New Stock                  ")
    print("                     8.Remove Existing Stock          ")
    print("                     9.Logout                         ")


# Main Code Starts From Here

# Selection Of Option from Menu
display_main()
selection = int(input("Please enter a menu option:"))


def submenu(user, pinno):
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

            pin_entered = input("Please enter your PIN number:")
            while pin_entered == pinno:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
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

            pin_entered = input("Please enter your PIN number:")
            while pin_entered == pinno:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
                mycur.execute(
                    "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                balance_report = mycur.fetchall()
                net_balance = int(balance_report[0]) - int(withdraw)
                mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                    str(net_balance), user))

        elif selec == 4:
            replyc = input("Are you sure? Y/N?:")
            while replyc.isalpha() == False:
                print("You've entered an invalid option.")
                replyc = input("Please enter a valid option:")
            else:
                if replyc.lower() == "y":
                    print()
                    mycur.execute(
                        "DELETE FROM USERS WHERE USERNAME = '{}'".format(user))
                else:
                    print()

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
            stock_to_be_bought = input(
                "Please enter the stock's name you wish to purchase:")

            mycur.execute("SELECT STKNAME FROM STOCKS;")
            stock_names = mycur.fetchall()
            while stock_to_be_bought not in stock_names:
                print("This stock does not exist!")
                print("Please choose from the above mentioned stocks or add new stock.")
                add_new_stock = input("Add new Stock? Y/N?")
                while add_new_stock.isalpha() == False:
                    print("You've entered an invalid option.")
                    add_new_stock = input("Please enter a valid option:")
                if add_new_stock.lower() == "y":
                    print("You've returned to the main menu")
                else:
                    stock_to_be_bought = input(
                        "Please enter the stock's name from the above mentioned names:")
            else:
                pin_entered = input("Please enter your PIN number:")
                while pin_entered == pinno:
                    print("The entered pin is incorrect.")
                    pin_entered = input("Please enter your correct pin:")
                else:
                    mycur.execute(
                        "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                    balance_report = mycur.fetchall()
                    net_balance = int(balance_report[0]) - int(withdraw)
                    mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                        str(net_balance), user))

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
            stksym = input("Please enter a symbol for the stock:")
            while stksym.isalpha() == False:
                print("You've entered an invalid symbol.")
                stksym = input(
                    "Please enter a valid symbol for the stock:")

            print(stkval)

            mycur.execute(
                "INSERT INTO STOCKS VALUES('{0}','{1}','{2}');".format(stkname.capitalize(), stkval, stksym.upper()))
            # mycon.commit()

            print(
                f"The {stkname} stock has been successfully added to the market!")

        elif selec == 8:

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

        elif selec == 9:
            print("You've successfully returned to the main menu!")
            break


# Main Loop
while True:
    if selection == 1:
        # For Username
        mycur.execute("SELECT USERNAME FROM USERS;")
        usernames = mycur.fetchall()
        usrname_existing = input("Please enter your username:")
        print()
        while usrname_existing not in usernames[0]:
            print("This user doesn't exist!")
            reply = input("New User? Y/N?")
            while reply.isalpha() == False:
                print("You've entered an invalid option.")
                reply = input("Please enter a valid option:")
            else:
                if reply.lower() == "y":
                    print("Then please do proceed to the sign up option.")
                    print()
                    break
                else:
                    usrname_existing = input(
                        "Please enter your username again:")
                    print()

        # For Password
        mycur.execute("SELECT PASSWD FROM USERS;")
        passwords = mycur.fetchall()
        pwd_existing = input("Please enter your password:")
        print()
        while pwd_existing not in passwords[0]:
            print("You've entered an incorrect password!")
            replyp = input("Forgot Password? Y/N?")
            while replyp.isalpha() == False:
                print("You've entered an invalid option.")
                replyp = input("Please enter a valid option:")
            else:
                if replyp.lower() == "y":
                    print("Then please enter the following details.")
                    print()

                    # Process
                    accno = input("Please enter your 10-digit account number:")

                    # Validating Account number
                    while accno.isnumeric() == False or len(accno) != 10:
                        print("You've entered an incorrent account number.")
                        accno = input("Please enter a valid account number:")

                    mycur.execute(
                        "SELECT ACCNO FROM USERS WHERE USERNAME = '{}'".format(usrname_existing))
                    accno_rec = mycur.fetchall()

                    while accno != accno_rec[0]:
                        print(
                            "Your account doesn't exist please create a new account!")
                        replya = input("New User? Y/N?")
                        while replya.isalpha() == False:
                            print("You've entered an invalid option.")
                            replya = input("Please enter a valid option:")
                        else:
                            if replya.lower() == "y":
                                print(
                                    "Then please do proceed to the sign up option.")
                                print()
                                break
                            else:
                                accno = input(
                                    "Please enter your account number again:")
                                print()
                                while accno.isnumeric() == False or len(accno) != 10:
                                    print(
                                        "You've entered an incorrent account number.")
                                    accno = input(
                                        "Please enter a valid account number:")

                    # Aadhar number
                    aadhar_no = input("Please enter your Aadhar number:")

                    while aadhar_no.isnumeric() == False:
                        print("You've entered an invalid Aadhar number.")
                        aadhar_no = input(
                            "Please enter a valid Aadhar number: ")

                    mycur.execute(
                        "SELECT AADHAR FROM USERS WHERE USERNAME = '{}';".format(usrname_existing))
                    aadhars_of_users = mycur.fetchall()

                    # Checking if Aadhar is repeated
                    while aadhar_no != aadhars_of_users[0]:
                        print(
                            "Your account doesn't exist please create a new account!")
                        replya = input("New User? Y/N?")
                        while replya.isalpha() == False:
                            print("You've entered an invalid option.")
                            replya = input("Please enter a valid option:")
                        else:
                            if replya.lower() == "y":
                                print(
                                    "Then please do proceed to the sign up option.")
                                print()
                                break
                            else:
                                accno = input(
                                    "Please enter your Aadhar number again:")
                                print()
                                while accno.isnumeric() == False or len(accno) != 10:
                                    print(
                                        "You've entered an incorrent Aadhar number.")
                                    accno = input(
                                        "Please enter a valid Aadhar number:")

                    # PIN number
                    print("Connecting...")
                    pin_no = int(input("Please enter your PIN No:"))

                    # Validating PIN number
                    while len(str(pin_no)) != 4:
                        print("Please Enter A Valid PIN")
                        pin_no = int(input("Please Enter Your PIN No:"))
                        break

                    mycur.execute(
                        "SELECT PINNO FROM USERS WHERE USERNAME = '{}';".format(usrname_existing))
                    pin_of_users = mycur.fetchall()

                    # Checking if Aadhar is repeated
                    while pin_no != pin_of_users[0]:
                        print(
                            "Your PIN No doesn't match!")
                        accno = input(
                            "Please enter your PIN No again:")
                        print()
                        while accno.isnumeric() == False or len(accno) != 4:
                            print(
                                "You've entered an incorrent PIN No.")
                            accno = input(
                                "Please enter a valid PIN No:")

                    pwd_new = input("Please enter new password:")
                    pwd_new1 = input("Please enter your password again:")

                    # Checking if the Passwords match
                    while pwd_new != pwd_new1:
                        print("Both The Passwords Do Not Match")
                        pwd_new = input("Please enter new password:")
                        pwd_new1 = input("Please enter your password again:")
                    else:
                        mycur.execute("UPDATE USERS SET PASSWD = '{}' WHERE USERNAME = '{}'".format(
                            pwd_new, usrname_existing))
                        print("Your Password has been set successfully!")

                else:
                    pwd_existing = input(
                        "Please enter your password again:")
                    print()

        else:
            mycur.execute(
                "SELECT PINNO FROM USERS WHERE USERNAME = '{}'".format(usrname_existing))
            pin_recs = mycur.fetchall()
            submenu(usrname_existing, pin_recs[0])

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
        # Checking if Username already exists
        while username.lower() in users:
            print("This username has already been taken.")
            username = input("Please Enter Another Username:")
        print()
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

        while bankname.isalpha() == False:
            print("You've entered an invalid name.")
            bankname = input("Please enter your real name: ")

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
            aad_reply = input("Existing User? Y/N?")
            while aad_reply.isalpha() == False:
                print("You've entered an invalid option.")
                aad_reply = input("Please enter a valid option:")
            else:
                if reply.lower() == "y":
                    print("Then please do proceed to the existing user option.")
                    print()
                    break
                else:
                    aadhar = input("Please enter your aadhar number again:")
                    print()

        # PIN number
        print("Connecting...")
        pin1 = int(input("Please enter a PIN No:"))
        pin2 = int(input("Please retype your PIN No to confirm:"))

        # Checking if the PIN No do match
        while pin1 != pin1:
            print("Both The PIN Numbers Do Not Match")
            pin1 = int(input("Please enter a PIN No:"))

            # Validating PIN number
            while len(str(pin1)) != 4:
                print("Please Enter A Valid PIN")
                pin1 = int(input("Please Enter Your PIN No:"))

            pin2 = int(input("Please retype your PIN No to confirm:"))

            # Validating PIN number
            while len(str(pin2)) != 4:
                print("Please Enter A Valid PIN")
                pin2 = int(input("Please Enter Your PIN No:"))
        else:
            print("Your Password has been set successfully!")

        # Balance
        balance = input(
            "Please enter amount of money you wish to deposit (in $):")

        while balance.isnumeric() == False:
            print("You've entered an invalid amount.")
            balance = input("Please Enter a valid amount:")

        mycur.execute(
            "INSERT INTO USERS VALUES ('{}','{}','{}','{}', '{}', '{}', '{}', '{}')".format(accno, bankname[0], str(pin1), name, username, pwd, aadhar, balance))
        print()
        print(
            f"You've successfully connected to your account {accno}, of {bankname[0]} bank and deposited ${balance} !")

        submenu(username, pin1)

    elif selection == 3:
        break

    else:
        selection = int(input("Please Enter A Valid Menu Option:"))

    display_main()
    selection = int(input("Please enter a menu option:"))

print("You've exited the program successfully! Thank you for using Stock Arena!")
