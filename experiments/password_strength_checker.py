password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"]= uppercase

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Bad Password")