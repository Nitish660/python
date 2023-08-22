# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def calculate_earnings(shoe_sizes, customer_preferences):
    earnings = 0
    counter = Counter(shoe_sizes)
    
    for size, price in customer_preferences:
        if counter[size] > 0:
            earnings += price
            counter[size] -= 1
    
    return earnings

# Read input
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

customer_preferences = []
for _ in range(num_customers):
    size, price = map(int, input().split())
    customer_preferences.append((size, price))

# Calculate and print earnings
earnings = calculate_earnings(shoe_sizes, customer_preferences)
print(earnings)
