movie = input()
kids = 0
student = 0
standard = 0
counter = 0
movie_counter = 0

while movie != 'Finish':
    free_place = int(input())
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'kid':
            kids += 1
        elif ticket_type == 'student':
            student += 1
        else:
            standard += 1
        counter += 1
        movie_counter += 1
        if movie_counter == free_place:
            print(f"{movie} - {movie_counter / free_place * 100:.2f}% full.")
            break
        ticket_type = input()
    else:
        free_place = movie_counter / free_place * 100
        print(f"{movie} - {free_place:.2f}% full.")
    movie_counter = 0
    movie = input()
else:
    print(f"Total tickets: {counter}")
    print(f"{student / counter * 100:.2f}% student tickets.")
    print(f"{standard / counter * 100:.2f}% standard tickets.")
    print(f"{kids / counter * 100:.2f}% kids tickets.")
