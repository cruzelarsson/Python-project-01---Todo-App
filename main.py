while True:
    # gets user input and strip space chars from it
    user_action = input("Type add, show, edit, exit or mark completed task: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos  =  file.readlines()

            todos.append(todo)

            with open ("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show':

            with open("todos.txt", "r") as file:
                todos  =  file.readlines()


            new_todos = [item.strip("\n") for item in todos]

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
            number = number - 1

            with open("todos.txt", "r") as file:
                todos  =  file.readlines()

            new_todo = input ("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open ("todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of completed tasks: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list. "
            print(message)

        case 'exit':
            break

        case invalid_action:
            print("Please use the following commands:")

print("Bye!")



