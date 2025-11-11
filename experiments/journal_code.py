date = input("Enter today's date:")

mood = input("How was your mood today from 1 to 10? ")

thought = input("Enter the journal log: \n")

with open (f"../Journal/{date}.txt" , "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thought)