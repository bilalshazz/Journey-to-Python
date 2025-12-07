# To-Do List program
import time

print("\nWelcome to my 'To-Do List Program', I will help you arrange all your tasks.")

# User tasks will be added to these empty lists
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []
Sunday = []

days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] # Creating a dictionary for the lists

# Needed for the remove_task() function.
day_map = {
    "1": ("Monday", Monday),
    "monday": ("Monday", Monday),

    "2": ("Tuesday", Tuesday),
    "tuesday": ("Tuesday", Tuesday),

    "3": ("Wednesday", Wednesday),
    "wednesday": ("Wednesday", Wednesday),

    "4": ("Thursday", Thursday),
    "thursday": ("Thursday", Thursday),

    "5": ("Friday", Friday),
    "friday": ("Friday", Friday),

    "6": ("Saturday", Saturday),
    "saturday": ("Saturday", Saturday),

    "7": ("Sunday", Sunday),
    "sunday": ("Sunday", Sunday)
}

class ToDoList():
    def user_tasks():    # This function will allow the user to add tasks to their preferred days.
        while True:
            print("\nYou can use this program to add or remove a task from a day of you choice:\n")

            print("1. Monday")
            print("2. Tuesday")
            print("3. Wednesday")
            print("4. Thursday")
            print("5. Friday")
            print("6. Saturday")
            print("7. Sunday")
            print("8. Remove a Task (R)")          
            print("9. Quit (Q)")

            day = input("\nPlease enter the day you'd like to add this task to (1-7), or remove a task (R / 8), or Quit (Q / 9): ").lower()

            if day in ["1", "monday"]:
                task = input("\nPlease enter the task for Monday: ").capitalize()
                Monday.append(task)
                print(f"\nHere are your task(s) for Monday: {Monday}")

            elif day in ["2", "tueday"]:
                task = input("\nPlease enter the task for Tuesday: ").capitalize()
                Tuesday.append(task)
                print(f"\nHere are your task(s) for Tuesday: {Tuesday}")

            elif day in ["3", "wednesday"]:
                task = input("\nPlease enter the task for Wednesday: ").capitalize()
                Wednesday.append(task)
                print(f"\nHere are your task(s) for Wednesday: {Wednesday}")

            elif day in ["4", "thursday"]:
                task = input("\nPlease enter the task for Thursday: ").capitalize()
                Thursday.append(task)
                print(f"\nHere are your task(s) for Thursday: {Thursday}")
            
            elif day in ["5", "friday"]:
                task = input("\nPlease enter the task for Friday: ").capitalize()
                Friday.append(task)
                print(f"\nHere are your task(s) for Friday: {Friday}")
            
            elif day in ["6", "saturday"]:
                task = input("\nPlease enter the task for Saturday: ").capitalize()
                Saturday.append(task)
                print(f"\nHere are your task(s) for Saturday: {Saturday}")
            
            elif day in ["7", "sunday"]:
                task = input("\nPlease enter the task for Sunday: ").capitalize()
                Sunday.append(task)
                print(f"\nHere are your task(s) for Sunday: {Sunday}")

            elif day in ["8", "r", "remove"]:
                ToDoList.remove_task()
            
            elif day in ["9", "q", "quit"]:
                print("\nThanks for using my program. Goodbye!\n")
                quit()

            else:
                print("\nPlease enter a valid option: ")
                ToDoList.user_tasks()
            
            while True:
                choice = input("\nWould you like to add (1), remove (2) a task, Quit (Q / 3), or view your tasks (4)? ").lower()
                if choice in ["1", "add"]:
                    ToDoList.user_tasks()

                elif choice in ["2", "remove"]:
                    ToDoList.remove_task()

                elif choice in ["3", "q", "quit"]:
                    print("\nThanks for using the program. Goodbye!\n")
                    quit()

                elif choice in ["4", "v", "view"]:
                    view_day = input("\nEnter the day you want to view tasks for (1-7): ").lower()
    
                    if view_day in ["1", "monday"]:
                        print(f"\nHere are your tasks for Monday: {Monday if Monday else "No Tasks!"}")
                    elif view_day in ["2", "tuesday"]:
                        print(f"\nHere are your tasks for Tuesday: {Tuesday if Tuesday else "No Tasks!"}")
                    elif view_day in ["3", "wednesday"]:
                        print(f"\nHere are your tasks for Wednesday: {Wednesday if Wednesday else "No Tasks!"}")
                    elif view_day in ["4", "thursday"]:
                        print(f"\nHere are your tasks for Thursday: {Thursday if Thursday else "No Tasks!"}")
                    elif view_day in ["5", "friday"]:
                        print(f"\nHere are your tasks for Friday: {Friday if Friday else "No Tasks!"}")
                    elif view_day in ["6", "saturday"]:
                        print(f"\nHere are your tasks for Saturday: {Saturday if Saturday else "No Tasks!"}")
                    elif view_day in ["7", "sunday"]:
                        print(f"\nHere are your tasks for Sunday: {Sunday if Sunday else "No Tasks!"}")
                    else:
                        print("\nInvalid input.")

                else:
                    print("\nInvalid option! Please try again.")

    def remove_task():  # This function will allow the user to remove a task of their choice, from a day of their choice.
        remove_from_day = input("\nPlease enter the day to remove a task from (1-7), or go back (B), or clear all tasks (C): ").lower()
        
        if remove_from_day in day_map:
            day_name, day_list = day_map[remove_from_day]

            if not day_list:
                print(f"\nNo tasks for {day_name}.")
                return

            print(f"\nHere are your tasks for {day_name}:\n")
            for i, task in enumerate(day_list, 1):
                print(f"{i}. {task}")

            while True:

                choice = input("\nEnter the number of the task you want to delete: ")

                if choice.isdigit() and 1 <= int(choice) <= len(day_list):
                    removed = day_list.pop(int(choice) - 1)
                    print(f"\nTask removed: {removed}")
                    print(f"\nUpdated tasks for '{day_name}': {day_list if day_list else 'No Tasks Left.'}")
                    break

                else:
                    print("\nInvalid choice!")

        elif remove_from_day in ["b", "back", "go back"]:
            ToDoList.user_tasks()

        elif remove_from_day in ["c", "clear", "clear all tasks"]:  # This removes all tasks
            are_your_sure = input("\nAre you sure you want to clear all tasks (This will delete all tasks from all the days), --- (Y / N): ").upper()
            if are_your_sure in ["Y", "YES"]:
                days.clear()
                print("\nAll tasks have been deleted.")
                print("\nThe program will end in: ")
                print("\n3...")
                time.sleep(1)
                print("\n2...")
                time.sleep(1)
                print("\n1...")
                time.sleep(1) 
                print("\nThanks for using my program. Goodbye!\n")
                quit()

            elif are_your_sure in ["N", "NO"]:
                print("\nYou have decided not to delete any tasks. \nGoing back: ")
                print("\n3...")
                time.sleep(1)
                print("\n2...")
                time.sleep(1)
                print("\n1...")
                time.sleep(1) 
                ToDoList.remove_task()

        else:
            print("\nPlease enter a valid option: ")
            ToDoList.remove_task()

ToDoList.user_tasks()

