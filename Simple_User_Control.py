print("**********\nUser Login\n**********\n")

sys_user = "erkinb" 

sys_pass  = "12345" 

user_name = input("Enter Username: ") 

password =  input("Enter Your Password: ")

if (user_name != sys_user and password == sys_pass):
    print("Wrong Username")
elif (user_name == sys_user and password != sys_pass):
    print("Wrong Password")

elif (user_name != sys_user and password != sys_pass):
    print("Username and Password Wrong")

else:
    print("You have successfully logged in")