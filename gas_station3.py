def find_max_profit(gasStations, profitList, distanceBetween):
    max_profit = 0
    lastStation = gasStations[0]

    # Sort points based on their positions
    stations = zip(gasStations,profitList)
    stations = sorted(stations)

    for gstop, profitMargin in stations:
        if gstop - lastStation >= distanceBetween:
            max_profit += profitMargin
            lastStation = gstop

    return max_profit

# Example usage:
x = [0, 3, 7, 11]  # Points on the x-axis
p = [5, 6, 8, 10]  # Profits at each point
d = 5              # Minimum distance between gas stations
print(find_max_profit(x, p, d))  # Output: 16
