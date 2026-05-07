guests = ['Wife', 'Mother']
print(guests)

message = f"{guests[0]}, Let's have dinner?"
print(message)

message = f"{guests[0]}, Cannot make it."

guests.pop(0)
guests.insert(0, "Niha")
print(guests)

guests.insert(0,"brother")
guests.insert(2,"cousin")
guests.append("Father in law")

print(guests)

print("You can only two people for dinner")
popped_item = guests.pop()
message = f"Hi {popped_item}, I am sorry to unable to inviting to dinner"
print(message)

popped_item = guests.pop()
message = f"Hi {popped_item}, I am sorry to unable to inviting to dinner"
print(message)

popped_item = guests.pop()
message = f"Hi {popped_item}, I am sorry to unable to inviting to dinner"
print(message)

print(guests)

message = f"Hi {guests[0]}, you are invited to dinner"
print(message)

message = f"Hi {guests[1]}, you are invited to dinner"
print(message)

del guests[0]
del guests[0]

print(guests)