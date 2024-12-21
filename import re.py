import re

password_pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])(?=.{6,}).+$' #?= anywhere for 1 or more occurence
#\d is a digit

password=input("Enter your password here:")
if re.match(password_pattern,password):
    print("You have successfully created your password")
else:
    print("Your password is weak. Try again")