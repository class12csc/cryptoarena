# Importing Modules And Performing Basic Operations
import mysql.connector as ms
mycon = ms.connect(host="localhost", user="root", passwd="root")
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS CRYPTO")
mycon = ms.connect(host="localhost", user="root",
                   passwd="root", database="crypto")

# Printing of menu

print("******************************************************")
print("         -------------------------------------        ")
print("                 Welcome To Crypto Arena              ")
print("               Your Turn To Become Richer             ")
print("         -------------------------------------        ")
print("******************************************************")
print("\n\n\n")
print("                     1.Existing User? Login           ")
print("                     2.New User? Sign Up              ")
print("                     3.Exit                           ")


# Main Code Starts From Here


# Selection Of Option from Menu
selection = int(input("Please Enter A Menu Option:"))

# Main Loop
while True:
    if selection == 1:
        pass
    elif selection == 2:
        pass
    elif selection == 3:
        break
    else:
        selection = int(input("Please Enter A Valid Menu Option:"))

print("You've Exited The Program Successfully!")
