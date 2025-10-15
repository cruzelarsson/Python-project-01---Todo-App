
while True:
    user_action = input("Type add, show, edit, exit or mark completed task: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case 'show':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            #new_todos = [item.strip("\n") for item in todos]

            #new_todos = []

           #for item in todos:
                #new_item = item.strip("\n")
                #new_todos.append(new_item)

            for index , item in enumerate(todos):

                item = item.strip("\n")

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



