"""
The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
Let's begin!
"""
from time import sleep, strftime
YOUR_NAME = "YOUR_NAME"
calendar = {}

def welcome():
  print("Hello" + YOUR_NAME + ".")
  print("Calendar starting")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("It is: " + strftime("%H : %M : %S"))
  print("What would you like to do ?")

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print("Calendar is empty.")
      else:
        print(calendar)
    elif user_choice == 'U':
      date = input("What date ?")
      update = input("Enter the update:")
      calendar[date] = update
      print("Update was succesfull")
      print(calendar)
    elif user_choice == 'A':
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10) or int(date[6:]) < int(strftime("%Y")):
          print("You entered an invalid date")
          try_again = input("Do you  want to try again ? Y for Yes, N for No")
          try_again = try_again.upper()
          if try_again == 'Y':
              continue
          else:
              start == False
      else:
          calendar[date] = event
          print("Event was succesfully added")
          print(calendar)
    elif user_choice == 'D':
        if len(calendar.keys()) < 1:
          print("Calendar is empty")
        else:
          event = input("What event?")
          for date in calendar.keys():
            if event == calendar[date]:
              del calendar[date]
              print("Event was succesfully deleted")
              print(calendar)
            else:
              print("Incorrect event was specified")
    elif user_choice == 'X':
        start == False
    else:
        print("Invalid command was entered!")
        start == False

start_calendar()