# more examples for Match

name = input("Enter your name \n")
match name:
     case "dileep":
         print("Welcome dileep")
     case "Dilu":
         print("Welcome Dilu")
     case "Appu":
         print("Welcome Appu")
     case _:
         print("Hello Welcome!")
