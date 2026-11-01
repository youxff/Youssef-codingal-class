# School Subject Planner

subjects = {}

def add_subject():
    name = input("Enter subject name: ")
    subjects[name] = []
    print(f"{name} added successfully!\n")

def add_task():
    subject = input("Enter subject name: ")

    if subject in subjects:
        task = input("Enter homework/task: ")
        subjects[subject].append(task)
        print("Task added successfully!\n")
    else:
        print("Subject not found.\n")

def view_planner():
    if not subjects:
        print("No subjects added yet.\n")
        return

    print("\n--- SCHOOL SUBJECT PLANNER ---")
    for subject, tasks in subjects.items():
        print(f"\nSubject: {subject}")

        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")
        else:
            print("  No tasks assigned.")
    print()

while True:
    print("====== SCHOOL SUBJECT PLANNER ======")
    print("1. Add Subject")
    print("2. Add Task")
    print("3. View Planner")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_subject()
    elif choice == "2":
        add_task()
    elif choice == "3":
        view_planner()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")