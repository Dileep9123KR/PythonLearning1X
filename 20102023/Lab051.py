# Grade Calculator by Match - Failed due to conditions are not supported in match

score = int(input("Enter you score \n"))

# match score:
#     case 1:
#         if 90 >= score <= 100:
#             print("Grade A")
#     case 2:
#         if score >= 80 and score <= 89:
#             print("Grade B")
#     case 3:
#         if score >= 70 and score <= 79:
#             print("Grade C")
#     case 4:
#         if score >= 60 and score <= 69:
#             print("Grade D")
#     case 5:
#         if score >= 0 and score <= 59:
#             print("Grade F")
#     case _:
#         print("Please enter your score")

match score:
    case score >= 90 and score <= 100:
        print("Grade A")
    case score >= 80 and score <= 89:
        print("Grade B")
    case score >= 70 and score <= 79:
        print("Grade C")
    case score >= 60 and score <= 69:
        print("Grade D")
    case score >= 0 and score <= 59:
        print("Grade F")
    case _:
        print("Please enter your score")
