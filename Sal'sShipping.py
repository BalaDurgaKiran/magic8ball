# 1. Define the weight of the package
weight = 4.8  # Replace with the desired weight

# Ground Shipping
print("Ground Shipping:")
if weight <= 2:
    cost = weight * 1.5 + 20
    print(f"Cost for {weight} lb package: ${cost:.2f}")
elif 2 < weight <= 6:
    cost = weight * 3 + 20
    print(f"Cost for {weight} lb package: ${cost:.2f}")
elif 6 < weight <= 10:
    cost = weight * 4 + 20
    print(f"Cost for {weight} lb package: ${cost:.2f}")
else:
    cost = weight * 4.75 + 20
    print(f"Cost for {weight} lb package: ${cost:.2f}")

# 4. Cost of Ground Shipping Premium
ground_shipping_premium_cost = 125.00
print(f"\nGround Shipping Premium: ${ground_shipping_premium_cost:.2f}")

# Drone Shipping
print("\nDrone Shipping:")
if weight <= 2:
    cost = weight * 4.5
    print(f"Cost for {weight} lb package: ${cost:.2f}")
elif 2 < weight <= 6:
    cost = weight * 9
    print(f"Cost for {weight} lb package: ${cost:.2f}")
elif 6 < weight <= 10:
    cost = weight * 12
    print(f"Cost for {weight} lb package: ${cost:.2f}")
else:
    cost = weight * 14.25
    print(f"Cost for {weight} lb package: ${cost:.2f}")
