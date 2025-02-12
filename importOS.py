import os
if not os.path.isdir("cat"):
    os.mkdir("cat")
    os.chdir("cat")
print(os.getcwd())
with open("catsssss.txt", "w") as file:
    content=file.write("Cats are animalss\n Cats are cute\n Cats like to drink milk\n Cats are orange sometimes\n Cats hate dogs")

with open("catsssss.txt", "r") as file:
    contents=file.read()
    print(contents)
'''
with open("cats.txt", "w")as file:
    file.write("cats are animals")

try:
    with open("pig.txt", "r")as file:
    content=file.read()
except FileNotFoundError:
    print("File does not exist")
else:
    print("file contents")
    print(content)

with open("cats.txt", "r") as f:
    position = f.tell()
    print("Current position:", position)
    contents=f.read()
    print("file contents: ")
    print(contents)

with open("cats.txt", "r") as f:
    f.seek(5)
    data = f.read(5)
    print(data)
'''
