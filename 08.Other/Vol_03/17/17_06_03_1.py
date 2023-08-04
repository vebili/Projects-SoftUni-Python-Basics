def gather_credits(n_credit, *course):
    courses = []
    total = 0

    for c in course:
        name, credits = c

        if total >= n_credit:
            break

        if name not in courses:
            total += credits
            courses.append(name)

    if total >= n_credit:
        courses.sort()
        return f"Enrollment finished! Maximum credits: {total}.\nCourses: {', '.join(courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {n_credit - total} credits more."

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