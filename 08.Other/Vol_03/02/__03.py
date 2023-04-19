records = {}

capacity = int(input())

command = input()
while not command == "Statistics":
    command = command.split("=")
    if command[0] == "Add":
        username = command[1]
        sent_messages = int(command[2])
        received_messages = int(command[3])
        if username not in records:
            records[username] = {"sent": sent_messages, "received": received_messages}

    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in records and receiver in records:
            records[sender]["sent"] += 1
            records[receiver]["received"] += 1
        if records[sender]["sent"] + records[sender]["received"] >= capacity:
            print(f'{sender} reached the capacity!')
            records.pop(sender)
        if records[receiver]["sent"] + records[receiver]["received"] >= capacity:
            print(f'{receiver} reached the capacity!')
            records.pop(receiver)

    elif command[0] == "Empty":
        user_to_clear = command[1]
        if user_to_clear in records:
            records[user_to_clear]["sent"] = 0
            records[user_to_clear]["received"] = 0
            records.pop(user_to_clear)
        if user_to_clear == "All":
            records={}

    command = input()

records = sorted(records.items(), key=lambda x: (-x[1]['received'], x[0]))

print(f"Users count: {len(records)}")
for user, data in records:
    print(f"{user} - {data['sent'] + data['received']}")
