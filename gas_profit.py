def max_profit(x, p, d):
#    n = len(x)
    max_profit = 0
    prev_station = x[0]

    # Sort points based on their positions
    points = zip(x, p)
    points = sorted(points)
    print("x", end=": ")
    print(x)
    print("p", end=": ")
    print(p)
    print("pts", end=": ")
    print(points)

    for pos, profit in points:
        if pos - prev_station >= d:
            max_profit += profit
            prev_station = pos

    return max_profit

# Example usage:
x = [0, 3, 7, 11]  # Points on the x-axis
p = [5, 6, 8, 10]  # Profits at each point
d = 5              # Minimum distance between gas stations
print(max_profit(x, p, d))  # Output: 16
