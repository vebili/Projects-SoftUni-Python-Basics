def solve_temple_challenge(tools, substances, challenges):
    while challenges:
        tool = tools[0]
        substance = substances[-1]
        result = tool * substance

        if result in challenges:
            tools.pop(0)
            substances.pop()
            challenges.remove(result)
        else:
            tools.append(tools.pop(0) + 1)
            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()

        if not tools or not substances:
            return False

    return True


def print_sequences(tools, substances, challenges):
    if not tools and not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        if substances:
            print("Substances:", ", ".join(map(str, substances)))
    else:
        print("Harry is lost in the temple. Oblivion awaits him.")
        if tools:
            print("Tools:", ", ".join(map(str, tools)))
        if challenges:
            print("Challenges:", ", ".join(map(str, challenges)))


tools = list(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

if solve_temple_challenge(tools, substances, challenges):
    print_sequences(tools, substances, challenges)
else:
    print_sequences(tools, substances, challenges)
