##import datetime, os
##def logactivity(user,action):
##    with open("logbook.txt", "a") as file:
##        time=datetime.datetime.now()
##        file.write(f'{user} performed {action}at {time}\n')
##
##logactivity("John", "login")
##with open("logbook.txt", "r") as file:
##    content=file.read()
##    print("file contents")
##    print(content)
import os
if os.path.exists("logbook.txt"):
    os.remove("logbook.txt")
    print("File deleted successfully")
else:
    print("File not found")
