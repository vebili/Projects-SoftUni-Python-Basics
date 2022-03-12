weight = float(input())
service_type = input()
distance = int(input())
price = 0.0

if service_type == "standard":
    if weight > 91.0:
        price += distance * 0.20
    elif 41.0 < weight < 91.0:
        price += distance * 0.15
    elif 11.0 < weight < 41.0:
        price += distance * 0.10
    elif 1.0 < weight < 11.0:
        price += distance * 0.05
    else:
        price += distance * 0.03
elif service_type == "express":
    if weight > 91.0:
        price += (distance * ((0.20 * 0.01) * weight)) + (distance * 0.20)
    elif 41.0 < weight < 91.0:
        price += (distance * ((0.15 * 0.02) * weight)) + (distance * 0.15)
    elif 11.0 < weight < 41.0:
        price += (distance * ((0.10 * 0.05) * weight)) + (distance * 0.10)
    elif 1.0 < weight < 11.0:
        price += (distance * ((0.05 * 0.40) * weight)) + (distance * 0.05)
else:
    price += (distance * ((0.05 * 0.80) * weight)) + (distance * 0.05)
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
