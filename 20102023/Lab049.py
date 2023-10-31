# Match
# Similar to switch in Java

num = int(input("Enter a number \n"))

match num:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case _: # default is used as underscore _
        print("No idea.!")

