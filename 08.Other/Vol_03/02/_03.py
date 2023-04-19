capacity = int(input())
users = {}
while True:
    command = input().split("=")
    if command[0] == "Statistics":
        break
    elif command[0] == "Add":
        username = command[1]
        send = int(command[2])
        received = int(command[3])
        if username not in users:
            users[username] = [send, received]
    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1
            if sum(users[sender]) >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if sum(users[receiver]) >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]
    elif command[0] == "Empty":
        user_or_all = command[1]
        if user_or_all == "All":
            users.clear()
        elif user_or_all in users:
            del users[user_or_all]
print(f"Users count: {len(users)}")
for user, messages in sorted(users.items(), key=lambda x: (-(x[1][1]), x[0])):
    print(f"{user} - {sum(messages)}")
