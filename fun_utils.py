import os
import datetime

def run_command(command):
  return os.system(command)


def check_datetime():
  return datetime.datetime.today()

today = check_datetime()
print(today)



run_command("date") # calling a function
run_command("df -h") # calling a function