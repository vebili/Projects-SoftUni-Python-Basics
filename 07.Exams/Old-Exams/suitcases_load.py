capacity = float(input())
volume_bag = input()
total_volume = 0
bag_counter = 0
bags_in_plane = 0
while volume_bag != 'End':
    bag_counter += 1
    volume_bag = float(volume_bag)
    if bag_counter == 3:
        bag_counter = 0
        volume_bag *= 1.1
    total_volume += volume_bag
    if total_volume > capacity:
        print(f"No more space!")
        break
    bags_in_plane += 1
    volume_bag = input()
if total_volume <= capacity:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {bags_in_plane} suitcases loaded.")
