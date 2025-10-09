todos = []

while True:
    user_action = input("Type add, show, edit, exit or mark completed task: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for index , item in enumerate(todos):
                row = f"{index+1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input ("Enter the new todo: ")
            todos[number-1] = new_todo
            print(todos[number-1])

        case 'complete':
            number = int(input("Number of completed tasks: "))
            todos.pop(number-1)

        case 'exit':
            break

        case invalid_action:
            print("Please use the following commands:")

print("Bye!")



