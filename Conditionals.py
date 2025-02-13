#using upper() and lower()

day_of_week= input("Enter the day of week: ").lower() #anything you enter will be converted into lower case only
# print(day_of_week)

if day_of_week=="saturday" or day_of_week=="sunday":
  print("Weekend")
else:
  print("Not weekend")

  #Calcualtion using condaitonals
  

num1= int(input("Enter num1: "))
num2 =int(input("Enter num2: "))

choice = input("Enter the operation: (Options + , -, *, /,%) ")

if choice == "+":
  addition=num1+num2
  print("addition",addition)
elif choice == "-":
  subtraction=num1-num2
  print("subtraction",subtraction)
elif choice == "*":
  multiplication=num1*num2
  print("multiplication",multiplication)
elif choice == "/":
  division=num1/num2
  print("division",division)
elif choice == "%":
  remainder=num1%num2
  print("remainder",remainder)
else:
  print("Invalid choice")