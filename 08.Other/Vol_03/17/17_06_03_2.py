def gather_credits(credits, *args):
    needed_credits = credits
    total_credits = 0
    courses = []
    for arg in args:
        if needed_credits > 0:
            if arg[0] not in courses:
                courses.append(arg[0])
                total_credits += int(arg[1])
                needed_credits -= int(arg[1])
            else:
                continue
        else:
            break
    result = ''
    if needed_credits <= 0:
        result += f"Enrollment finished! Maximum credits: {total_credits}.\n"
        result += f"Courses: {', '.join(sorted(courses))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {credits - total_credits} credits more."


    return result
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