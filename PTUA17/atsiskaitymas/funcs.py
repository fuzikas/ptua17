import json
from operator import itemgetter


try:
    with open ("tasks.json", "r") as my_file:
        my_list = json.load(my_file)
except json.JSONDecodeError:
    my_list = []

def adding_task()->None:
    my_task = input("What task would you like to add? ")
    task_category = input("What is the category of this task? (Work/Personal) ")
    due_date = input("What is a due date for this task? (e.g 05.04.24) ")
    priority = int(input("How would you like to prioritize this task? (1 = High, 2 = Medium, 3= Low) "))
    my_list.append({"Task":my_task.lower(), "Category":task_category, "Due date":due_date,"Priority":priority, "Done":False})
    with open ("tasks.json", "w") as my_file:
         json.dump(my_list, my_file, indent=4)

def listing_tasks()->None:
     with open("tasks.json", "r") as file:
        my_list = json.load(file)
        for i in my_list:
            if i["Done"] == False:
                print(i["Task"],"[]")
            elif i["Done"] ==True:
                print(i["Task"],"[✔]")


def removing_tasks(task_index:int)->None:
    user_friendly_number = task_index-1
    my_list.pop(user_friendly_number)
    with open ("tasks.json", "w") as my_file:
        json.dump(my_list, my_file, indent=4)


def completing_task(task_index:int)->None:
    user_friendly_number = task_index-1
    my_list[user_friendly_number]["Done"] =True
    with open ("tasks.json", "w") as my_file:
        json.dump(my_list, my_file, indent=4)



def sorting_by_rating()->None:
    sorted_tasks = sorted(my_list, key=itemgetter("Priority"))
    print(sorted_tasks)

def finding_tasks()->None:
    desired_task = input("What task you are interested in? ").lower
    try:
        for task in my_list:
            if task["Task"]==desired_task:
                print(task)
    except Exception as e:
        print(e)


