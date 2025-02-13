#using upper() and lower()

day_of_week= input("Enter the day of week: ").lower() #anything you enter will be converted into lower case only
# print(day_of_week)

if day_of_week=="saturday" or day_of_week=="sunday":
  print("Weekend")
else:
  print("Not weekend")

  #Calcualtion using condaitonals
  

choice = input("Enter the operation: (Options + , -, *, /,%) ")

if choice == "+":
  print("addition")
elif choice == "-":
  print("subtraction")
elif choice == "":
  print("multiplication")
elif choice == "/":
  print("division")
elif choice == "%":
  print("remainder")
else:
  print("Invalid choice")