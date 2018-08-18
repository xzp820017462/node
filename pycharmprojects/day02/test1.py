# IMPORT GETPASS

import getpass

USERNAME = input("USERNAME:")
PASSWORD = getpass.getpass("PASSWORD")
if USERNAME == "BOB" and PASSWORD == "123456":
    print('LOGIN SUCCESSFUL')
else:
    print("LOGIN INORRECT")






