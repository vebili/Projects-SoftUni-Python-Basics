needed_experience = float(input())
battles_count = int(input())
current_experience = 0

managed = False

for battle in range(1, battles_count + 1):
    new_experience = float(input())
    current_experience += new_experience
    if battle % 3 == 0:
        current_experience += new_experience * 0.15
    if battle % 5 == 0:
        current_experience -= new_experience * 0.1
    if current_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        managed = True
        break

if not managed:
    print(f"Player was not able to collect the needed experience, "
          f"{(needed_experience - current_experience):.2f} more needed.")
