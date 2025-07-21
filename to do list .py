to_do_list=[]
def show_menu():
    print("--- TO-DO LIST MENU---")
    print("1. to show all task")
    print("2. to add task")
    print("3. to delete task")
    print("4. to quit todo")
def add_task():
    task=input("please enter the task you want to add :")
    to_do_list.append(task)
    print("task added")

def show_task():
    if len(to_do_list)==0:
        print("your to-do list is empty.")
    else:
        print("\n your task:")
        for i in range(len(to_do_list)):
            print(f"{i+1} {to_do_list[i]}")

def delete_task():
    show_task()
    try:
        task_num=int(input(" Enter task number to delete: "))
        if 1<= task_num<=len(to_do_list):
            del to_do_list[task_num-1]
            print("Task deleted.")
        else:
            print("Invaild task number")
    except ValueError:
        print("please enter a vaild number.")
print( show_menu())
while(True):
    choice=input("choose a number(1-4): ")
    if(choice=='1'):
        show_task()
    elif (choice =='2'):
        add_task()
    elif (choice =='3'):
        delete_task()
    elif (choice =='4'):
        print("quitting todo!!")
        break
    elif ():
        print("Invaild choice please choose an between 1-5")


