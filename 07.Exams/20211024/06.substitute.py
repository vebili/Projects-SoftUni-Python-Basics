k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0
is_over_count = False

for s1 in range(k, 8 + 1):
    for s2 in range(9, l - 1, - 1):
        for s3 in range(m, 8 + 1):
            for s4 in range(9, n - 1, - 1):
                if s1 % 2 == 0 and s2 % 2 != 0 and s3 % 2 == 0 and s4 % 2 != 0:
                    if s1 != s3 or s2 != s4:
                        print(f"{s1}{s2} - {s3}{s4}")
                        count += 1
                        if count == 6:
                            is_over_count = True
                            break
                    else:
                        print(f"Cannot change the same player.")

                if is_over_count:
                    break
            if is_over_count:
                break
        if is_over_count:
            break
    if is_over_count:
        break
