print("Menu")
print("Create a file\n1.Read a file\n2.Append a file\n3.Quit\n")
name=input("Write file name")
file=open(name, "w")
wr=input("Write something in the file")
file.write(wr)
file.close()
while True:    
    choice=input("Enter your choice(1-4):")
    if choice=="1":
        file=open(name, "r")
        content=file.read()
        print("file contents\n")
        print(content)
        file.close()
    elif choice=="2":
        file=open(name, "a")
        e=input("Write something in the file")
        file.write(e)
        file.close()
    elif choice=="3":
        print("Thank you")
        break 
    else:
        print("Enter valid number between 1-4")
