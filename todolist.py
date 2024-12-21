#todolist
def entertodo():
    todo={} #user entering todo:time
    while True:
        choice=input("Enter A to add an event or Q to quit").upper()
        if choice=='Q':
            break
        elif choice=='A':
            event=input("Enter event name: ").capitalize()
            time=int(input("Enter time: "))
            todo.update({event:time})
        else:
            print("Invalid choice")
                    
    return todo



