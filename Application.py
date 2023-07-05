import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank",
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()


# cursor.execute("SELECT * FROM logindetails")

# rows = cursor.fetchall()
#

# for row in rows:
#     print(row)
#

# cursor.close()
# connection.close()




class Userlogin:

    def check_username_exists(self,username):
        query = "SELECT * FROM logindetails WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            return True
        else:
            return False

    def verify_password(self,password):
        query="SELECT * FROM logindetails WHERE password = %s"
        cursor.execute(query,(password,))
        row =cursor.fetchone()
        if row:
            return True
        else:
            return False



    def login(self):
        username=input("Please Enter your username to login: ")
        if not self.check_username_exists(username):
            print("you have enter wrong credentials !!!")
            return
        password = input("Please enter your password: ")
        if not self.verify_password( password):
            print("Invalid password. Please try again.")
            return

        print("Login successful!")


class Options:
    def menu(self):
        initial_balance = 40000
        choice = None  # Initialize choice outside the loop

        while choice != "3":  # Loop until user chooses option 3 (Exit)
            print("1. Deposit money")
            print("2. Check balance")
            print("3. Exit")

            choice = input("Please choose your option: ")

            if choice == "1":
                initial_balance = self.deposit(initial_balance)
            elif choice == "2":
                print("Balance:", initial_balance)
            elif choice == "3":
                print("Exiting the program...")
            elif not choice:
                print("No input received. Displaying menu options again.")
            else:
                print("Invalid choice. Please try again.")

            print()

    def deposit(self, balance):
        amount = int(input("Please enter the amount you would like to deposit: "))
        print(amount, "has been deposited into your account")
        balance += amount
        print("Your balance is", balance)
        return balance















my_obj=Userlogin()
my_obj.login()
options = Options()
options.menu()