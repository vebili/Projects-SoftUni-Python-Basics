n = int(input())
integers = [int(num) for num in input().split()]

integers_to_remove = max(integers)

while integers_to_remove in integers:
    integers.remove(integers_to_remove)

print(max(integers))
