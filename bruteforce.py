from itertools import combinations

# Function to calculate total value and weight of a given combination
def calculate_value_weight(combination, val, wt):
    total_value = sum(val[i] for i in combination)
    total_weight = sum(wt[i] for i in combination)
    return total_value, total_weight

# Function to find all possible combinations of items and return the best one
def knapSackBruteForce(W, wt, val, n, items):
    max_value = 0
    best_combination = []
    all_combinations = []

    # Check all possible combinations of items
    for r in range(n + 1):
        for combination in combinations(range(n), r):
            total_value, total_weight = calculate_value_weight(combination, val, wt)
            comb_items = [items[i] for i in combination]
            all_combinations.append((comb_items, total_value, total_weight))
            if total_weight <= W and total_value > max_value:
                max_value = total_value
                best_combination = combination

    return max_value, best_combination, all_combinations

# Driver code
if __name__ == "__main__":
    # Get input from user
    n = int(input("Enter number of items: "))

    val = []
    wt = []
    items = []

    for i in range(n):
        item_name = input(f"Enter name of item {i+1}: ")
        v = int(input(f"Enter value of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        items.append(item_name)
        val.append(v)
        wt.append(w)

    W = int(input("Enter maximum weight capacity of the knapsack: "))

    # Find the best combination using brute force
    max_val, best_combination, all_combinations = knapSackBruteForce(W, wt, val, n, items)

    # Output all combinations
    print("\nAll possible combinations (item names, total value, total weight):")
    for comb_items, total_value, total_weight in all_combinations:
        print(f"Items: {comb_items}, Total Value: {total_value}, Total Weight: {total_weight}")

    # Output the maximum value and the best combination
    best_comb_items = [items[i] for i in best_combination]
    print(f"\nMaximum Profit that can we get = {max_val}")
    print("Items included in the best combination:", best_comb_items)
