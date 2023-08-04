def gather_credits(needed_credits, *courses):
    enrolled_courses = set()
    gathered_credits = 0

    for course in courses:
        course_name, course_credits = course

        if gathered_credits >= needed_credits:
            break

        if course_name not in enrolled_courses:
            enrolled_courses.add(course_name)
            gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        enrolled_courses_sorted = sorted(enrolled_courses)
        courses_str = ', '.join(enrolled_courses_sorted)
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {courses_str}"
    else:
        credits_shortage = needed_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
