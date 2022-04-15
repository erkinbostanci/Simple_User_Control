print("**********\nUser Login\n**********\n")

sys_user = "erkinb" 

sys_pass  = "12345" 

hv_left = 3
while True:
    user_name = input("Enter Username: ") 
    password =  input("Enter Your Password: ")
    if (user_name != sys_user and password == sys_pass):
        print("Wrong Username")
        hv_left -= 1
        print('Right of Entry: ',hv_left)
    elif (user_name == sys_user and password != sys_pass):
        print("Wrong Password")
        hv_left -= 1
        print('Right of Entry: ',hv_left)
    elif (user_name != sys_user and password != sys_pass):
        print("Username and Password Wrong")
        hv_left -= 1
        print('Right of Entry: ',hv_left)
    else:
        print("You have successfully logged in")
        break
    if (hv_left == 0 ):

        print("Your Entry Right Is Over")
        break