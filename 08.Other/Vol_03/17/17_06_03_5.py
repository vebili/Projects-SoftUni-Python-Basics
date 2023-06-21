def gather_credits(need_credits, *args):
    result = []
    curses = {}
    total_credits = 0
    for arg in args:
        if not arg[0] in curses:
            curses[arg[0]] = int(arg[1])
        total_credits += curses[arg[0]]
        if need_credits < total_credits:
            result.append(f"Enrollment finished! Maximum credits: {total_credits}.")
            break
    if need_credits > total_credits:
        current_credits = need_credits - total_credits
        return f"You need to enroll in more courses! You have to gather {current_credits} credits more."
    sorted_curses = sorted(curses.keys())

    result.append(f"Courses: {sorted_curses}")

    return "\n".join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))