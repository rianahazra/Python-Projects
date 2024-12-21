import time
'''
file=open("cat.txt", "w")
file.write("Cats like to eat rats\n")
file.write("\trats do not like cats")
file.close()
'''
with open("cats.txt", "w")as file:
    file.write("cats are animals")

with open("cats.txt", "r")as file:
    content=file.read()
    print("file contents")
    print(content)

'''
file=open("cat.txt", "a")
file.write("\nCats like to drink milk")

file.close()

file=open("cat.txt", "r")
content=file.read()
print("file contents\n")
print(content)
file.close()
file=open("cat.txt", "r")
for line in file:
    print(line.strip())
    time.sleep(1)
file.close()
'''
