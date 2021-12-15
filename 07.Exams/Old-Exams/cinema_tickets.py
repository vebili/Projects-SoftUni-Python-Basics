movie_name = input()
student = 0
standard = 0
kid = 0
total_tickets = 0
tickets_per_movie = 0
while movie_name != 'Finish':
    places = int(input())
    for place in range(places):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        else:
            kid += 1
        tickets_per_movie += 1
    total_tickets += tickets_per_movie
    print(f"{movie_name} - {tickets_per_movie / places * 100:.2f}% full.")
    tickets_per_movie = 0
    movie_name = input()
print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")
