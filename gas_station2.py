def find_max_profit(gasStations, profitsPerStation, distanceBetweenStations):
    bestProfit = 0
    last_station = profitsPerStation[0]

    # pair the station with its profit and sort it
    stations = zip(gasStations, profitsPerStation)
    stations = sorted(stations)

    print("x",end=": ")
    print(gasStations)
    print("p",end=": ")
    print(profitsPerStation)
    print("pts",end=": ")
    print(stations)

    # visit each station and tally the best profit margin
    for gstop, profitMargin in stations:
         if distanceBetweenStations <= gstop - last_station:
           bestProfit += profitMargin
           last_station = gstop

    return bestProfit

stations = [0, 3, 7, 11]
profits = [5, 6, 8, 10]
distance = 5
print(find_max_profit(stations,profits,distance))

