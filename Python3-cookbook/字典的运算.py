prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# min_price = sorted(zip(prices.values(),prices.keys()))
# print min_price

prices_and_names = zip(prices.values(), prices.keys())
print prices_and_names
print(min(prices_and_names))
print(max(prices_and_names))