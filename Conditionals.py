#using upper() and lower()

day_of_week= input("Enter the day of week: ").lower() #anything you enter will be converted into lower case only
# print(day_of_week)

if day_of_week=="saturday" or day_of_week=="sunday":
  print("Weekend")
else:
  print("Not weekend")