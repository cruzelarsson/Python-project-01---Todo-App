todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                item = item.title()
                print(item)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input ("Enter the new todo: ")
            todos[number-1] = new_todo
            print(todos[number-1])

        case 'exit':
            break

        case invalid_action:
            print("Please use the following commands:")

print("Bye!")



