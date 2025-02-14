import getpass

stored_username = "admin"
stored_password = "secure123"

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

if username == stored_username and password == stored_password:
	print("Access Granted. Welcome!")
else:
	print("Access Denied. Incorrect username or password.")
