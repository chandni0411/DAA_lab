def knapsack(W, price, wt):
    n = len(price)
    ratio = []

    for i in range(n):
        ratio.append((price[i] / wt[i], i))
    ratio.sort(reverse=True)

    total = 0
    items = []

    for r, id in ratio:
        if wt[id] <= W:
            W -= wt[id]
            total += price[id]
            items.append((id, wt[id], price[id]))
        else:
            fraction = W / wt[id]
            total += price[id] * fraction
            items.append((id, W, price[id] * fraction))
            break

    return total, items

# Example
W = 50
price = [60, 100, 120]
wt = [10, 20, 30]

result = knapsack(W, price, wt)
print(result)
