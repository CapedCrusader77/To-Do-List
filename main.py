todo_list = []

def show_menu():
	print("\nTo-Do List Menu:")
	print("1. Add task")
	print("2. View tasks")
	print("3. Remove task")
	print("4. Exit")

while True:
	show_menu()
	choice = input("Enter your choice (1-4): ")

	if choice == "1":
		task = input("Enter a new task: ")
		todo_list.append(task)
		print("Task added.")
	elif choice == "2":
		print("\nYour To-Do List:")
		for idx, task in enumerate(todo_list, 1):
			print(f"{idx}. {task}")
	elif choice == "3":
		print("\nYour To-Do List:")
		for idx, task in enumerate(todo_list, 1):
			print(f"{idx}. {task}")
		try:
			remove_idx = int(input("Enter the number of the task to remove: "))
			if 1 <= remove_idx <= len(todo_list):
				removed = todo_list.pop(remove_idx - 1)
				print(f"Removed: {removed}")
			else:
				print("Invalid task number.")
		except ValueError:
			print("Please enter a valid number.")
	elif choice == "4":
		print("Goodbye!")
		break
	else:
		print("Invalid choice. Please try again.")
