while True:
    # gets user input and strip space chars from it
    user_action = input("Type add, show, edit, exit or mark completed task: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos  =  file.readlines()

        todos.append(todo + "\n")

        with open ("todos.txt", "w" ) as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("todos.txt", "r") as file:
            todos  =  file.readlines()


        #new_todos = [item.strip("\n") for item in todos]

        #new_todos = []
       #for item in todos:
            #new_item = item.strip("\n")
            #new_todos.append(new_item)

        for index , item in enumerate(todos):

            item = item.strip("\n")

            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action [5:])
            number = number - 1

            with open("todos.txt", "r") as file:
                todos  =  file.readlines()

            new_todo = input ("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            with open ("todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid")
            continue #goes back to the beginning of the code, and prints out the input command

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list. "
            print(message)
        except IndexError:
            print("Out of bound")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Please use the following commands:")


print("Bye!")



