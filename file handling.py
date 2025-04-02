tasks = []


# ✅ File path
file_path = "tasks.txt"

# ✅ Search function
def search_log():
    keyword = input("\n🔍 Enter keyword to search in log: ").strip().lower()

    # ✅ Open file in read mode
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    found = False

    # ✅ Loop through log file
    for line in lines:
        if keyword in line.lower():
            print(f"✅ Found: {line.strip()}")
            found = True

    if not found:
        print("❌ Not found!")





# ✅ Task add karne ka function
def add_task():
    """Naya task add karne ka function"""
    task = input("\n📝 Enter task: ")
    tasks.append(task)
    print(f"✅ Task added: {task}")





# ✅ Tasks ko file me save karne ka function
def save_task():
    """Tasks ko file me save karne ka function"""
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("💾 Tasks saved successfully!")




# ✅ Tasks ko dekhne ka function
def view_tsak():
    """Tasks ko dekhne ka function"""
    try:
        with open("tasks.txt", "r") as f:
            content = f.read()
            if content:
                print("\n📄 Saved Tasks:")
                print(content)
            else:
                print("❌ No tasks saved yet.")
    except FileNotFoundError:
        print("❌ No saved tasks found.")    


# ✅ Task delete karne ka function
def delete_task():
    """Task delete karne ka function"""
    if tasks:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        try:
            index = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f"❌ Task deleted: {deleted_task}")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Enter a valid number.")
    else:
        print("❌ No tasks to delete.")




def edit_task():
    """Task edit karne ka function"""
    if tasks:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):  # Tasks ko list karega
            print(f"{i}. {task}")

        try:
            index = int(input("\nEnter task number to edit: ")) - 1  # User input le raha hai
            if 0 <= index < len(tasks):  # Validity check kar raha hai
                new_task = input("✏️ Enter new task: ")  # Naya task input le raha hai
                tasks[index] = new_task  # Task replace kar raha hai
                print(f"✅ Task updated: {new_task}")  # Success message
            else:
                print("⚠️ Invalid task number.")  # Agar invalid input ho toh error
        except ValueError:
            print("⚠️ Enter a valid number.")  # Agar number na ho toh error
    else:
        print("❌ No tasks to edit.")  # Agar list empty ho toh message



# ✅ Program exit karne ka function
def exit_program():
    """Program exit karne ka function"""
    print("🚀 Exiting... Bye!")
    exit()




while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Save Tasks")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Search Log")
    print("6. Edit Task")
    print("7. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "4":
        delete_task()

    elif choice == "2":
        save_task()

    elif choice == "3":
        view_tsak()

    elif choice == "5":
        search_log()

    elif choice == "6":
        edit_task()
    elif choice == "7":
        exit_program()    

    else:
        print("Invalid choice. Please try again.")

        
