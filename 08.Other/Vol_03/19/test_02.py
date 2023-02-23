all_friends = input().split(", ")

while True:
    command = input().split()
    if command[0] == "Report":
        break

    elif command[0] == "Blacklist":
        name = command[1]
        if name not in all_friends:
            print(f"{name} was not found.")
        else:
            index_name = all_friends.index(name)
            all_friends[index_name] = "Blacklisted"
            print(f"{name} was blacklisted.")

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(all_friends):
            if all_friends[index] != "Blacklisted" and all_friends[index] != "Lost":
                name = all_friends[index]
                all_friends[index] = "Lost"
                print(f"{name} was lost due to an error.")

    elif command[0] == "Change":
        index, new_name = int(command[1]), command[2]
        if 0 <= index < len(all_friends):
            current_name = all_friends[index]
            all_friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")


print(f"Blacklisted names: {len([name for name in all_friends if name == 'Blacklisted'])}")
print(f"Lost names: {len([name for name in all_friends if name == 'Lost'])}")
print(*all_friends)