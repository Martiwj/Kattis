def vurder_veier(wind_speed, roads):
    results = []

    for road, max_safe_speed in roads:
        if wind_speed <= max_safe_speed:
            results.append(f"{road} opin")
        else:
            results.append(f"{road} lokud")

    return results


wind_speed = int(input())

num_roads = int(input())


roads_data = []
for _ in range(num_roads):
    road, max_safe_speed = input().split()
    max_safe_speed = int(max_safe_speed)
    roads_data.append((road, max_safe_speed))


resultater = vurder_veier(wind_speed, roads_data)


for resultat in resultater:
    print(resultat)
