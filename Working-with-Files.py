import os

# https://github.com/justsyntex

while True:
    ans = input("\nHello! How can I help you?\n"
          "\n1. Create file"
          "\n2. Delete file"
          "\n3. Create folder"
          "\n4. Delete folder\n\n")


    if ans == "1":
        name = input("Write name of file: ")

        file = open(name, "w+")
        file.close()
    elif ans == "2":
        name = input("Write name of file: ")

        os.remove(name)
    elif ans == "3":
        name = input("Write name of folder: ")

        os.makedirs(name, exist_ok=True)
    elif ans == "4":
        name = input("Write name of folder: ")

        os.rmdir(name)