def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    todo_list=[]
    while True:
        display_menu()
        choice=input("Choose an option (1-4):")
        
        if choice=='1':
            task=input("Enter the task:")
            todo_list.append(task)
            print("--------------------")
            print(f"Task '{task}' added!")
            print("--------------------")
        elif choice=='2':
            if not todo_list:
                print("your todo_list is empty!")
            else:
                print("\nYour Tasks:")
                print("--------------------")
                for index, task in enumerate(todo_list,start=1):
                    print(f"{index}.{task}")
            print("--------------------")
        
        elif choice=='3':
            if not todo_list:
                print('your todo-list is empty!')
            else:
                task_number=int(input("Enter the task number to remove:"))
                if 1<=task_number<=len(todo_list):
                    removed_task=todo_list.pop(task_number-1)
                    print("--------------------")
                    print(f"Task '{removed_task}'removed!")
                    print("--------------------")
                else:
                    print("Invalid Task Number!!")
        
        elif choice=='4':
            print("**************************")
            print("Exiting the TO-DO List application.")
            print("**************************")
            print("Thank You!!")
            break
        else:
            print('Invalid choice. Please choose a valid option.')
if __name__=="__main__":
    main()
