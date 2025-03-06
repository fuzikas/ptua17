from funcs import *



def list_manager():
    while True:
        choice = int(input(("===== To-Do List Manager ===== \n 1.Add task \n 2.View tasks \n 3.Mark task as completed \n 4.Remove task \n 5.Sort tasks by their rating \n 6.Find a task using its name \n 7.Exit \n Enter your choice: ")))
        try:

         if choice == 1:
            try:
                adding_task()
            except ValueError:
                print("Failed to add, make sure that input an integer for Priority(1 = High, 2 = Medium, 3 = Low)")
         elif choice ==2:
                listing_tasks()
         elif choice ==3:
                task_index = int(input(f"Which task would you like to mark as completed? Enter index of the task (starting from 1) {my_list} "))
                completing_task(task_index)
                print(f"Task nr. {task_index} was sucesffully completed")
         elif choice ==4:
                task_index = int(input("Which task would you like to remove? "))
                removing_tasks(task_index)
         elif choice == 5:
            sorting_by_rating()
         elif choice ==6:
            finding_tasks()
         elif choice ==7:
            break
         else:
             print("Number must be between 1 and 7")
        except Exception as e:
           print(f"Operation can not be completed because of {e}")



list_manager()