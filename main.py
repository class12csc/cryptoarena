# Importing Modules And Performing Basic Operations
import math
import mysql.connector as ms
import random
mycon = ms.connect(host="localhost", user="root",
                   passwd="root")
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS FINANCE;")
mycur.execute("USE FINANCE;")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS USERS (ACCNO VARCHAR(10) NOT NULL, BANKNAME VARCHAR(90) NOT NULL, PINNO CHAR(4) NOT NULL, NAME VARCHAR(90) NOT NULL, USERNAME VARCHAR(90) PRIMARY KEY, PASSWD VARCHAR(90) NOT NULL, AADHAR VARCHAR(12), BALANCE VARCHAR(18));")
mycur.execute(
    "CREATE TABLE IF NOT EXISTS STOCKS (STKNAME VARCHAR(90) PRIMARY KEY, VALUE CHAR(90) NOT NULL, SYMBOL CHAR(9) NOT NULL);")


def inserting_vals():
    # Inserting default Stock values
    mycur.execute("INSERT INTO STOCKS VALUES('Apple','139','AAPL');")
    mycur.execute(
        "INSERT INTO STOCKS VALUES('Saudi Aramco', '9.13', '2222.sr')")
    mycur.execute("INSERT INTO STOCKS VALUES('Microsoft', '221.36', 'MSFT')")
    mycur.execute("INSERT INTO STOCKS VALUES('Google', '86.70', 'GOOG')")
    mycur.execute("INSERT INTO STOCKS VALUES('Amazon', '90.98', 'AMZN')")
    mycur.execute("INSERT INTO STOCKS VALUES('Tesla', '207.47', 'TSLA')")
    mycur.execute(
        "INSERT INTO STOCKS VALUES('Berkshire Hathway', '287', 'BRK')")
    mycur.execute(
        "INSERT INTO STOCKS VALUES('Unitded Health', '538.71', 'UNH')")
    mycur.execute("INSERT INTO STOCKS VALUES('Exxon Mobil', '112.31', 'XOM')")
    mycur.execute("INSERT INTO STOCKS VALUES('Johnson', '171.48', 'JNJ')")
    mycur.execute("INSERT INTO STOCKS VALUES('Visa', '196.98', 'V')")
    mycur.execute("INSERT INTO STOCKS VALUES('JPMorgan', '130.58', 'JPM')")
    mycur.execute("INSERT INTO STOCKS VALUES('Walmart', '140.97', 'WMT')")
    mycur.execute("INSERT INTO STOCKS VALUES('Nvidia', '141.56', 'NVDA')")
    mycur.execute("INSERT INTO STOCKS VALUES('Chevron', '183.42', 'CVX')")
    mycur.execute("INSERT INTO STOCKS VALUES('Eli Lilly', '357.41', 'LLY')")
    mycur.execute("INSERT INTO STOCKS VALUES('LVMH', '663.61', 'MCPA')")
    mycur.execute("INSERT INTO STOCKS VALUES('TSCM', '62.48', 'TSM')")

    # Inserting one default User
    mycur.execute(
        "INSERT INTO USERS VALUES('1234567890','Chase','1234','Admin','admin','admin','1234','1200');")

    mycon.commit()


# # To prevent Data Overlap Error in MYSQL(repeated entries)
try:
    inserting_vals()
except ms.errors.IntegrityError:
    pass


# Functions used

def introductory_display():
    print("\n\n\n")
    print("******************************************************")
    print("         -------------------------------------        ")
    print("              Welcome To The Finance Broker           ")
    print("               Your Turn To Become Richer             ")
    print()
    print("                 By Tushar and Nischit                ")
    print("         -------------------------------------        ")
    print("******************************************************")


# Printing of menu
introductory_display()


def display_main_user():
    print("\n\n\n")
    print("                          Main Menu                   ")
    print("                     1.Existing User? Login           ")
    print("                     2.New User? Sign Up              ")
    print("                     3.Exit                           ")
    print("\n\n\n")


def display_main():
    print("\n\n\n")
    print("                          Main Menu                   ")
    print("                     1.Admin Login                    ")
    print("                     2.User Login                     ")
    print("                     3.Exit                           ")
    print("\n\n\n")


def display_submenu_admin():
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


def display_submenu():
    print("                        Account Menu                  ")
    print("                     1.Show Balance                   ")
    print("                     2.Deposit Money                  ")
    print("                     3.Withdraw Money                 ")
    print("                     4.Show Available Stocks          ")
    print("                     5.Buy New Stock                  ")
    print("                     6.Logout                         ")


def stock_val_update():
    rand_no = round(random.random(), 2)
    add_sub = ['+', '-']
    rand_op = random.choice(add_sub)
    if rand_op == '+':
        mycur.execute(
            "UPDATE STOCKS SET VALUE = VALUE + '{}'".format(rand_no))
        mycon.commit()
    else:
        mycur.execute(
            "UPDATE STOCKS SET VALUE = VALUE -'{}'".format(rand_no))
        mycon.commit()


stock_val_update()

# Selection Of Option from Menu
display_main()
selection = input("Please enter a menu option:")


def display_stocks():
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
                try:
                    value = round(float(j), 2)
                    spaces = 30 - len(str(value))
                    print(value, end=" " * spaces)
                except ValueError:
                    spaces = 30 - len(j)
                    print(j, end=" " * spaces)
            print()


def add_stk():
    # Stock name
    stkname = input("Please enter stock name:")
    while stkname.isalpha() == False:
        print("Please enter a valid name.")
        stkname = input("Please enter the real name of the stock: ")

    mycur.execute("SELECT STKNAME FROM STOCKS;")
    stocks_existing = mycur.fetchall()
    temp_list_stocks = []
    for i in stocks_existing:
        for j in i:
            temp_list_stocks.append(j.lower())

    while stkname.lower() in temp_list_stocks:
        print("Stock already exists!")
        break
    else:
        return stkname


def stk_details(stockname):
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

    mycur.execute(
        "INSERT INTO STOCKS VALUES('{0}','{1}','{2}');".format(stockname.capitalize(), stkval, stksym.upper()))
    # mycon.commit()

    print(
        f"{stockname.capitalize()} stock has been successfully added to the market!")


new_var_selec = 0

# Admin credentials
admin_un = "admin"
admin_pass = "admin"


def submenu_admin(user, pinno):
    while True:
        """
        1) Show balance
        2) Show available stock
        3) Buy Stock
        4) Add
        5) Remove
        6) Return to Main Menu

        """
        global new_var_selec

        try:
            int(selec)
        except UnboundLocalError:
            print("\n\n\n")
            display_submenu_admin()
            print("\n\n\n")
            selec = input("Please enter a menu option:")

        if new_var_selec != 0:
            infloop_prev = selec
        else:
            infloop_prev = '18'

        if infloop_prev == selec:
            print("\n\n\n")
            display_submenu_admin()
            print("\n\n\n")
            selec = input("Please enter a menu option:")

        if selec == '1':
            # Diplaying Balance
            mycur.execute(
                "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
            balance_report = mycur.fetchall()
            print(f"This is your current balance ${balance_report[0][0]}.")

        elif selec == '2':
            deposit = input("Please enter amount of money to be deposited:")

            while deposit.isnumeric() == False:
                print("You've entered an invalid amount.")
                deposit = input("Please enter a valid amount: ")

            pin_entered = input("Please enter your PIN number:")
            while pin_entered != pinno[0]:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
                mycur.execute(
                    "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                balance_report = mycur.fetchall()
                net_balance = float(balance_report[0][0]) + float(deposit)
                mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                    str(net_balance), user))
                print(f"Your current balance is: ${net_balance}")
            mycon.commit()

        elif selec == '3':
            withdraw = input("Please enter amount of money to be withdrawn:")

            while withdraw.isnumeric() == False:
                print("You've entered an invalid amount.")
                withdraw = input("Please enter a valid amount: ")

            pin_entered = input("Please enter your PIN number:")
            while pin_entered != pinno[0]:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
                mycur.execute(
                    "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                balance_report = mycur.fetchall()
                net_balance = float(balance_report[0][0]) - float(withdraw)
                if net_balance < 0:
                    print(
                        f"You've insufficient amount ${math.fabs(net_balance)}!")
                else:
                    mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                        str(net_balance), user))
                    print(f"Your current balance is: ${net_balance}")
            mycon.commit()

        elif selec == '4':
            user_del = input("Enter username to be deleted:")
            while user_del.isspace() == True or user_del == "":
                print("You've entered an invalid username.")
                user_del = input("Please enter a valid username:")
            else:
                mycur.execute("SELECT USERNAME FROM USERS;")
                users_del_list = mycur.fetchall()
                temp_list_users_del = []
                for i in users_del_list:
                    for j in i:
                        temp_list_users_del.append(j)
                while user_del.lower() not in temp_list_users_del:
                    print("This username doesn't exist.")
                    user_del = input("Please Enter another username:")
                print()

            replycu = input("Are you sure? Y/N?:")
            while replycu.isalpha() == False or replycu.lower() not in ['y', 'n']:
                print("You've entered an invalid option.")
                replycu = input("Please enter a valid option:")
            else:
                if replycu.lower() == "y":
                    print()
                    mycur.execute(
                        "DELETE FROM USERS WHERE USERNAME = '{}'".format(user_del))
                    print(
                        f"{user_del.capitalize()} account has been deleted successfully. Thank you for being with Stock Arena!")
                    mycon.commit()

                    break
                else:
                    print()

        elif selec == '5':
            display_stocks()

        elif selec == '6':
            display_stocks()
            print()

            stock_to_be_bought = input(
                "Please enter the stock's name you wish to purchase:")
            while stock_to_be_bought.isalpha() == False:
                print("You've entered an invalid stock name.")
                stock_to_be_bought = input("Please enter a valid stock name:")

            mycur.execute("SELECT STKNAME FROM STOCKS;")
            stock_names = mycur.fetchall()
            temp_list = []
            for i in stock_names:
                for j in i:
                    temp_list.append(j.lower())
            while stock_to_be_bought.lower() not in temp_list:
                print("This stock does not exist!")
                print("Please choose from the above mentioned stocks or add new stock.")
                add_new_stock = input("Add new Stock? Y/N?:")

                while add_new_stock.isalpha() == False or add_new_stock.lower() not in ['y', 'n']:
                    print("You've entered an invalid option.")
                    add_new_stock = input("Please enter a valid option:")

                if add_new_stock.lower() == "y":
                    stockname_returned = add_stk()
                    if stockname_returned != None:
                        stk_details(stockname_returned)
                    mycon.commit()
                    break
                else:
                    stock_to_be_bought = input(
                        "Please enter the stock's name from the above mentioned names:")
            else:
                quantity = float(input(
                    f"Please enter quantity of {stock_to_be_bought.capitalize()}:"))
                while math.ceil(quantity) != math.floor(quantity) or quantity < 1:
                    while str(quantity).isnumeric() == False:
                        print("You've entered an invalid stock quantity.")
                        quantity = float(input(
                            "Please enter a valid stock quantity:"))
                        if math.ceil(quantity) == math.floor(quantity):
                            break

                pin_entered = input("Please enter your PIN number:")
                while pin_entered != pinno[0]:
                    print("The entered pin is incorrect.")
                    pin_entered = input("Please enter your correct pin:")
                else:
                    mycur.execute(
                        "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                    balance_report = mycur.fetchall()
                    mycur.execute(
                        "SELECT VALUE FROM STOCKS WHERE STKNAME = '{}'".format(stock_to_be_bought))
                    stock_value = mycur.fetchall()
                    net_balance = float(
                        balance_report[0][0]) - (float(quantity) * float(stock_value[0][0]))
                    if net_balance < 0:
                        print(
                            f"You've insufficient amount ${math.fabs(net_balance)}!")
                    else:
                        mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                            str(net_balance), user))
                        print()
                        print(
                            f"You've successfully bought {stock_to_be_bought} for a price of ${float(quantity) * float(stock_value[0][0])}.")
                        print(f"Your updated balance is $ {str(net_balance)}")
                    mycon.commit()

        elif selec == '7':
            stockname_returned = add_stk()
            if stockname_returned != None:
                stk_details(stockname_returned)
            mycon.commit()

        elif selec == '8':
            display_stocks()
            print()

            # Validating the Stock name
            stkrem = input(
                "Please enter the stock's name that has to be removed from the listing:")
            while stkrem.isalpha() == False:
                print("Please enter a valid name.")
                stkrem = input("Please enter the real name of the stock: ")
            mycur.execute(
                "SELECT * FROM STOCKS WHERE STKNAME = '{}'".format(stkrem.capitalize()))
            stkrec = mycur.fetchall()

            # Checking and Deleting The Stock
            if len(stkrem) == 0:
                print("No such stock exists.")

            else:
                mycur.execute(
                    "DELETE FROM STOCKS WHERE STKNAME = '{}'".format(stkrem))
                print(
                    f"The {stkrem.capitalize()} has been successfully removed from the listing!")
            mycon.commit()

        elif selec == '9':
            print("You've successfully returned to the main menu!")
            new_var_selec = 0
            break

        else:
            options_list = []
            for i in range(1, 10):
                options_list.append(str(i))
            while selec not in options_list:
                selec = input("Please Enter A Valid Menu Option:")
                new_var_selec = -1
            print()

        new_var_selec += 1
        stock_val_update()


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
        global new_var_selec

        try:
            int(selec)
        except UnboundLocalError:
            print("\n\n\n")
            display_submenu()
            print("\n\n\n")
            selec = input("Please enter a menu option:")

        if new_var_selec != 0:
            infloop_prev = selec
        else:
            infloop_prev = '18'

        if infloop_prev == selec:
            print("\n\n\n")
            display_submenu()
            print("\n\n\n")
            selec = input("Please enter a menu option:")

        if selec == '1':
            # Diplaying Balance
            mycur.execute(
                "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
            balance_report = mycur.fetchall()
            print(f"This is your current balance ${balance_report[0][0]}.")

        elif selec == '2':
            deposit = input("Please enter amount of money to be deposited:")

            while deposit.isnumeric() == False:
                print("You've entered an invalid amount.")
                deposit = input("Please enter a valid amount: ")

            pin_entered = input("Please enter your PIN number:")
            while pin_entered != pinno[0]:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
                mycur.execute(
                    "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                balance_report = mycur.fetchall()
                net_balance = float(balance_report[0][0]) + float(deposit)
                mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                    str(net_balance), user))
                print(f"Your current balance is: ${net_balance}")
            mycon.commit()

        elif selec == '3':
            withdraw = input("Please enter amount of money to be withdrawn:")

            while withdraw.isnumeric() == False:
                print("You've entered an invalid amount.")
                withdraw = input("Please enter a valid amount: ")

            pin_entered = input("Please enter your PIN number:")
            while pin_entered != pinno[0]:
                print("The entered pin is incorrect.")
                pin_entered = input("Please enter your correct pin:")
            else:
                mycur.execute(
                    "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                balance_report = mycur.fetchall()
                net_balance = float(balance_report[0][0]) - float(withdraw)
                if net_balance < 0:
                    print(
                        f"You've insufficient amount ${math.fabs(net_balance)}!")
                else:
                    mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                        str(net_balance), user))
                    print(f"Your current balance is: ${net_balance}")
            mycon.commit()

        elif selec == '4':
            display_stocks()

        elif selec == '5':
            display_stocks()
            print()

            stock_to_be_bought = input(
                "Please enter the stock's name you wish to purchase:")
            while stock_to_be_bought.isalpha() == False:
                print("You've entered an invalid stock name.")
                stock_to_be_bought = input("Please enter a valid stock name:")

            mycur.execute("SELECT STKNAME FROM STOCKS;")
            stock_names = mycur.fetchall()
            temp_list = []
            for i in stock_names:
                for j in i:
                    temp_list.append(j.lower())
            while stock_to_be_bought.lower() not in temp_list:
                print("This stock does not exist!")
                print("Please choose from the above mentioned stocks or add new stock.")
                add_new_stock = input("Add new Stock? Y/N?:")

                while add_new_stock.isalpha() == False or add_new_stock.lower() not in ['y', 'n']:
                    print("You've entered an invalid option.")
                    add_new_stock = input("Please enter a valid option:")

                if add_new_stock.lower() == "y":
                    stockname_returned = add_stk()
                    if stockname_returned != None:
                        stk_details(stockname_returned)
                    mycon.commit()
                    break
                else:
                    stock_to_be_bought = input(
                        "Please enter the stock's name from the above mentioned names:")
            else:
                quantity = float(input(
                    f"Please enter quantity of {stock_to_be_bought.capitalize()}:"))
                while math.ceil(quantity) != math.floor(quantity) or quantity < 1:
                    while str(quantity).isnumeric() == False:
                        print("You've entered an invalid stock quantity.")
                        quantity = float(input(
                            "Please enter a valid stock quantity:"))
                        if math.ceil(quantity) == math.floor(quantity):
                            break

                pin_entered = input("Please enter your PIN number:")
                while pin_entered != pinno[0]:
                    print("The entered pin is incorrect.")
                    pin_entered = input("Please enter your correct pin:")
                else:
                    mycur.execute(
                        "SELECT BALANCE FROM USERS WHERE USERNAME = '{}';".format(user))
                    balance_report = mycur.fetchall()
                    mycur.execute(
                        "SELECT VALUE FROM STOCKS WHERE STKNAME = '{}'".format(stock_to_be_bought))
                    stock_value = mycur.fetchall()
                    net_balance = float(
                        balance_report[0][0]) - (float(quantity) * float(stock_value[0][0]))
                    if net_balance < 0:
                        print(
                            f"You've insufficient amount ${math.fabs(net_balance)}!")
                    else:
                        mycur.execute("UPDATE USERS SET BALANCE = '{}' WHERE USERNAME = '{}'".format(
                            str(net_balance), user))
                        print()
                        print(
                            f"You've successfully bought {stock_to_be_bought} for a price of ${float(quantity) * float(stock_value[0][0])}.")
                        print(f"Your updated balance is $ {str(net_balance)}")
                    mycon.commit()

        elif selec == '6':
            print("You've successfully returned to the main menu!")
            new_var_selec = 0
            break

        else:
            options_list = []
            for i in range(1, 10):
                options_list.append(str(i))
            while selec not in options_list:
                selec = input("Please Enter A Valid Menu Option:")
                new_var_selec = -1
            print()

        new_var_selec += 1
        stock_val_update()


mycon.commit()
new_var = 1
new_var_u = 1


def sign_up():
    print("Please enter the following details:-")

    # Name
    name = input("Please Enter Your Name: ")
    while name.isalpha() == False:
        print("You've entered an invalid name.")
        name = input("Please enter your real name: ")

    print()

    # Username
    username = input("Please enter a username: ")
    while username.isspace() == True or username == "":
        print("You've entered an invalid username.")
        username = input("Please enter a valid username:")
    else:
        mycur.execute("SELECT USERNAME FROM USERS;")
        users = mycur.fetchall()
        temp_list_usernames = []
        for i in users:
            for j in i:
                temp_list_usernames.append(j)

        # Checking if Username already exists
        while username.lower() in temp_list_usernames:
            print("This username has already been taken.")
            username = input("Please Enter another username:")
        print()

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

    print()

    # Bank Details + Connection
    bankname = input("Please Enter Your Bank Name:")

    while bankname.isalpha() == False:
        print("You've entered an invalid name.")
        bankname = input("Please enter a valid bank name: ")

    # Checking for 'Bank' at the end
    banktest = bankname.split()
    if banktest[-1].lower() == "bank":
        del banktest[-1]
        "".join(banktest)
    bankname = banktest

    print()

    # Process
    accno = input("Please enter your 10-digit account number:")

    # Validating Account number
    while accno.isnumeric() == False or len(accno) != 10:
        print("You've entered an incorrent account number.")
        accno = input("Please enter a valid account number:")

    print()

    # Aadhar number
    aadhar = input("Please enter your Aadhar number:")

    while aadhar.isnumeric() == False:
        print("You've entered an invalid Aadhar number.")
        aadhar = input("Please enter a valid Aadhar number: ")

    mycur.execute("SELECT AADHAR FROM USERS;")
    aadhars_of_users = mycur.fetchall()

    # Checking if Aadhar is repeated
    while username.lower() in users:
        print("This Aadhar has already exists.")
        aad_reply = input("Existing User? Y/N?")
        while aad_reply.isalpha() == False or aad_reply.lower() not in ['y', 'n']:
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

    print()

    # PIN number
    print("Connecting...")
    pin1 = input("Please enter a PIN No:")
    while len(pin1) != 4 or pin1 == "":
        print("Please Enter A Valid PIN")
        pin1 = input("Please Enter Your PIN No:")

    pin2 = input("Please retype your PIN No to confirm:")
    while len(pin2) != 4 or pin2 == "":
        print("Please Enter A Valid PIN")
        pin2 = input("Please Enter Your PIN No:")

    print()

    # Checking if the PIN No do match
    while pin1 != pin2:
        print("Both The PIN Numbers Do Not Match")
        pin1 = input("Please enter a PIN No:")

        # Validating PIN number
        while len(pin1) != 4:
            print("Please Enter A Valid PIN")
            pin1 = input("Please Enter Your PIN No:")

        pin2 = input("Please retype your PIN No to confirm:")

        # Validating PIN number
        while len(pin2) != 4:
            print("Please Enter A Valid PIN")
            pin2 = input("Please Enter Your PIN No:")
    else:
        print("Your PIN No has been set successfully!")

    print()

    # Balance
    balance = input(
        "Please enter amount of money you wish to deposit (in $):")

    try:
        float(balance)
    except ValueError:
        while balance.isnumeric() == False:
            print("You've entered an invalid amount.")
            balance = input("Please Enter a valid amount (in $):")

    balance = balance.lstrip("0")

    mycur.execute(
        "INSERT INTO USERS VALUES ('{}','{}','{}','{}', '{}', '{}', '{}', '{}')".format(accno, bankname[0], pin1, name, username, pwd, aadhar, balance))
    print()
    print(
        f"You've successfully connected to your account {accno}, of {bankname[0]} bank and deposited ${balance} !")
    mycon.commit()
    pin_ls = []
    pin_ls.append(pin1)

    submenu(username, pin_ls)


# Main Loop
while True:

    if new_var == 1:
        new_var += 1
    else:
        display_main()
        selection = input("Please enter a menu option:")

    if selection == '1':
        usrname_existing_ad = input("Please enter the admin username:")
        while usrname_existing_ad != 'admin':
            print("This user doesn't exist!")
            usrname_existing_ad = input("Please enter a valid username:")

        pwd_existing_ad = input("Please enter the admin password:")
        while pwd_existing_ad != 'admin':
            print("The password entered is incorrect!")
            pwd_existing_ad = input("Please enter the correct password:")

        print()
        print("You've successfully logged in to the admin account!")

        pin_admin = ['1234']
        submenu_admin(admin_un, pin_admin)
        stock_val_update()

    elif selection == '2':
        while True:
            if new_var_u == 1:
                new_var_u += 1
            else:
                display_main_user()
                selection_u = input("Please enter a menu option:")

            if selection_u == '1':
                # For Username
                mycur.execute("SELECT USERNAME FROM USERS;")
                usernames = mycur.fetchall()
                temp_list_usn = []
                for i in usernames:
                    for j in i:
                        temp_list_usn.append(j)

                usrname_existing = input("Please enter your username:")

                while usrname_existing not in temp_list_usn:
                    print("This user doesn't exist!")
                    reply = input("New User? Y/N?:")
                    while reply.isalpha() == False or reply.lower() not in ['y', 'n']:
                        print("You've entered an invalid option.")
                        reply = input("Please enter a valid option:")

                    if reply.lower() == "y":
                        n = 0
                        sign_up()
                        break
                    else:
                        usrname_existing = input(
                            "Please enter your username again:")
                        print()
                n = 1
                if n == 0:
                    continue

                # For Password
                mycur.execute(
                    "SELECT PASSWD FROM USERS WHERE USERNAME = '{}';".format(usrname_existing))
                passwords = mycur.fetchall()
                pwd_existing = input("Please enter your password:")
                temp_list_pass = []
                for i in passwords:
                    for j in i:
                        temp_list_pass.append(j)
                print()

                while pwd_existing not in temp_list_pass:
                    print("You've entered an incorrect password!")
                    replyp = input("Forgot Password? Y/N?")
                    while replyp.isalpha() == False or replyp.lower() not in ['y', 'n']:
                        print("You've entered an invalid option.")
                        replyp = input("Please enter a valid option:")
                    else:
                        if replyp.lower() == "y":
                            print("Then please enter the following details.")
                            print()

                            # Process
                            accno = input(
                                "Please enter your 10-digit account number:")

                            # Validating Account number
                            while accno.isnumeric() == False or len(accno) != 10:
                                print("You've entered an incorrent account number.")
                                accno = input(
                                    "Please enter a valid account number:")

                            mycur.execute(
                                "SELECT ACCNO FROM USERS WHERE USERNAME = '{}'".format(usrname_existing))
                            accno_rec = mycur.fetchall()
                            temp_list_acc = []
                            for i in accno_rec:
                                for j in i:
                                    temp_list_acc.append(j)
                            while accno != str(temp_list_acc[0]):
                                print(
                                    "Your account doesn't exist please create a new account!")
                                replya = input("New User? Y/N?")
                                while replya.isalpha() == False or replya.lower() not in ['y', 'n']:
                                    print("You've entered an invalid option.")
                                    replya = input(
                                        "Please enter a valid option:")
                                else:
                                    if replya.lower() == "y":
                                        print()
                                        sign_up()
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
                            aadhar_no = input(
                                "Please enter your Aadhar number:")

                            while aadhar_no.isnumeric() == False:
                                print("You've entered an invalid Aadhar number.")
                                aadhar_no = input(
                                    "Please enter a valid Aadhar number: ")

                            mycur.execute(
                                "SELECT AADHAR FROM USERS WHERE USERNAME = '{}';".format(usrname_existing))
                            aadhars_of_users = mycur.fetchall()

                            # Checking if Aadhar is repeated
                            while aadhar_no != aadhars_of_users[0][0]:
                                print(
                                    "Your account doesn't exist please create a new account!")
                                replyc = input("New User? Y/N?")
                                while replyc.isalpha() == False or replyc.lower() not in ['y', 'n']:
                                    print("You've entered an invalid option.")
                                    replyc = input(
                                        "Please enter a valid option:")
                                else:
                                    if replyc.lower() == "y":
                                        print()
                                        sign_up()
                                        break
                                    else:
                                        accno = input(
                                            "Please enter your Aadhar number again:")
                                        print()
                                        while accno.isnumeric() == False:
                                            print(
                                                "You've entered an incorrent Aadhar number.")
                                            accno = input(
                                                "Please enter a valid Aadhar number:")

                            # PIN number
                            print("Connecting...")
                            pin_no = input("Please enter your PIN No:")

                            # Validating PIN number
                            while len(pin_no) != 4:
                                print("Please Enter A Valid PIN")
                                pin_no = input("Please Enter Your PIN No:")
                                break

                            mycur.execute(
                                "SELECT PINNO FROM USERS WHERE USERNAME = '{}';".format(usrname_existing))
                            pin_of_users = mycur.fetchall()

                            # Checking if the PIN Nos match
                            while pin_no != pin_of_users[0][0]:
                                print(
                                    "Your PIN No doesn't match!")
                                pin_no = input(
                                    "Please enter your PIN No again:")
                                print()
                                while pin_no.isnumeric() == False or len(pin_no) != 4:
                                    print(
                                        "You've entered an incorrent PIN No.")
                                    pin_no = input(
                                        "Please enter a valid PIN No:")

                            pwd_new = input("Please enter new password:")
                            pwd_new1 = input(
                                "Please enter your password again:")

                            # Checking if the Passwords match
                            while pwd_new != pwd_new1:
                                print("Both The Passwords Do Not Match")
                                pwd_new = input("Please enter new password:")
                                pwd_new1 = input(
                                    "Please enter your password again:")
                            else:
                                mycur.execute("UPDATE USERS SET PASSWD = '{}' WHERE USERNAME = '{}'".format(
                                    pwd_new, usrname_existing))
                                print("Your Password has been set successfully!")
                                print()
                                break

                        else:
                            pwd_existing = input(
                                "Please enter your password again:")
                            print()

                else:
                    print("You've successfully logged in to your account!")
                    if usrname_existing == admin_un and pwd_existing == admin_pass:
                        pin_admin = ['1234']
                        submenu_admin(admin_un, pin_admin)
                    else:
                        mycur.execute(
                            "SELECT PINNO FROM USERS WHERE USERNAME = '{}'".format(usrname_existing))
                        pin_recs = mycur.fetchall()
                        submenu(usrname_existing, pin_recs[0])

            elif selection_u == '2':
                sign_up()
                mycon.commit()

            elif selection == '3':
                break

            else:
                selection = input("Please Enter A Valid Menu Option:")
                new_var = 1
                print()

        stock_val_update()

    elif selection == '3':
        break

    else:
        selection = input("Please Enter A Valid Menu Option:")
        new_var = 1
        print()

    stock_val_update()


mycon.commit()
print()
print("You've exited the program successfully! Thank you for using Stock Arena!")
