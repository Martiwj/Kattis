
n = int(input())
prices = [int(input()) for _ in range(n)]

prices.sort(reverse=True)

total_price = sum(prices[i] for i in range(n) if i % 3 != 2)

print(total_price)