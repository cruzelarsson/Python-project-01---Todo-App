#custom function
def get_todos(filepath="todos.txt"): # Added default value for convenience
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def access_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    # gets user input and strip space chars from it
    user_action = input("Type add, show, edit, exit or mark completed task: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        #reads from the list
        todos = get_todos()

        todos.append(todo + "\n")

        #writes into the list
        access_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")


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

            todos = get_todos("todos.txt")

            new_todo = input ("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            access_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue #goes back to the beginning of the code, and prints out the input command

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            access_todos(todos)


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



