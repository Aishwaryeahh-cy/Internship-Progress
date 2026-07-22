# Smart City Traffic Analysis

traffic = []

for i in range(24):

    vehicles = int(input("Vehicles in Hour " + str(i) + ": "))

    traffic.append(vehicles)


print("\nTraffic Data")

print(traffic)


peak = max(traffic)

peak_hour = traffic.index(peak)

print("\nPeak Traffic Hour:", peak_hour)

print("Vehicles:", peak)


minimum = min(traffic)

min_hour = traffic.index(minimum)

print("\nMinimum Traffic Hour:", min_hour)

print("Vehicles:", minimum)


print("\nTotal Daily Traffic:", sum(traffic))


print("\nHours with Traffic Above 500")

for i in range(len(traffic)):

    if traffic[i] > 500:

        print("Hour", i, ":", traffic[i], "vehicles")