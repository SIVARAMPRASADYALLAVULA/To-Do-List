tasks=[]
while True:
  print("\n=====TO-DO LIST ====")
  print("1.Add Task")
  print("2.View Tasks")
  print("3.Remove Task")
  print("4.Exit")
choice=input("Enter your choice:")
if choice =="1":
  task=input("Enter task:")
  tasks.append(task)
  print("Task added successfully!")
elif choice=="2":
  if not tasks:
    print("No tasks available.")
  else:
    for i,task in enumerate(tasks,start=1):
       print(f"{i}.{task}")
elif choice=="3":
  if not tasks: 
     print("No tasks to remove.")
  else:
    for i,task in enumerate(tasks,start=1):
       print(f"{i}.{task}")
     try:
       task_num=int(input("Enter task number to remove:"))
       removed=tasks.pop(task_num-1)
       print(f"Removed:{removed}")
     except:
       print("Invalid task number.")
elif choice=="4":
  print("Exiting To-Do List")
  break
else:
  print(("Invalid choice.Try again.")
