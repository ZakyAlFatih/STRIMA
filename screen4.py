import streamlit as st

import streamlit as st

st.subheader("How many items do you want to input?")
itemtotal = st.number_input("Enter an integer for total items:", min_value=0, value=0, key="itemtotal")

st.subheader("Insert the maximum capacity?")
max_capacity = st.number_input("Enter an integer for max capacity:", min_value=0, value=0, key="max_capacity")

# List untuk menyimpan data
items = []
weights = []
profits = []

# Loop untuk mengambil input nama barang
for i in range(itemtotal):    
    itemname = st.text_input(f"Insert the item name for item {i+1}", key=f"name_{i}")
    items.append(itemname)

# Loop untuk mengambil input berat barang
for i in range(itemtotal):
    itemweight = st.number_input(f"Insert the weight for item {i+1}", key=f"weight_{i}", min_value=0.0, format="%.2f")
    weights.append(itemweight)

# Loop untuk mengambil input profit barang
for i in range(itemtotal):
    itemprofit = st.number_input(f"Insert the profit for item {i+1}", key=f"profit_{i}", min_value=0.0, format="%.2f")
    profits.append(itemprofit)

# Membuat tabel data
if itemtotal > 0:
    data = {
        "Name": items,
        "Weight": weights,
        "Profit": profits
    }
    st.table(data)
else:
    st.write("No items to display.")

# Fungsi untuk algoritma greedy
def greedy_algorithm(items_data, max_capacity, strategy):
    if strategy == "weight":
        sorted_items = sorted(items_data, key=lambda x: x['weight'])
    elif strategy == "profit":
        sorted_items = sorted(items_data, key=lambda x: x['profit'], reverse=True)
    elif strategy == "density":
        sorted_items = sorted(items_data, key=lambda x: x['profit'] / x['weight'], reverse=True)
    else:
        return [], 0, 0
    
    total_weight = 0
    total_profit = 0
    selected_items = []

    for item in sorted_items:
        if total_weight + item['weight'] <= max_capacity:
            selected_items.append(item)
            total_weight += item['weight']
            total_profit += item['profit']
        else:
            break

    return selected_items, total_weight, total_profit


#main program
if itemtotal > 0: 

    # Gabungkan semua informasi barang dalam satu list
    items_data = [{'name': items[i], 'weight': weights[i], 'profit': profits[i]} for i in range(itemtotal)]

    # Algoritma greedy by weight
    selected_items_weight, total_weight_weight, total_profit_weight = greedy_algorithm(items_data, max_capacity, "weight")

    # Algoritma greedy by profit
    selected_items_profit, total_weight_profit, total_profit_profit = greedy_algorithm(items_data, max_capacity, "profit")

    # Algoritma greedy by density
    selected_items_density, total_weight_density, total_profit_density = greedy_algorithm(items_data, max_capacity, "density")

    # Menampilkan hasil greedy by weight
    st.subheader("Selected Items by Weight")
    if selected_items_weight:
        selected_data_weight = {
            "Name": [item['name'] for item in selected_items_weight],
            "Weight": [item['weight'] for item in selected_items_weight],
            "Profit": [item['profit'] for item in selected_items_weight]
        }
        st.table(selected_data_weight)
        st.write(f"Total Weight: {total_weight_weight} kg")
        st.write(f"Total Profit: ${total_profit_weight}")
    else:
        st.write("No items selected.")

    # Menampilkan hasil greedy by profit
    st.subheader("Selected Items by Profit")
    if selected_items_profit:
        selected_data_profit = {
            "Name": [item['name'] for item in selected_items_profit],
            "Weight": [item['weight'] for item in selected_items_profit],
            "Profit": [item['profit'] for item in selected_items_profit]
        }
        st.table(selected_data_profit)
        st.write(f"Total Weight: {total_weight_profit} kg")
        st.write(f"Total Profit: ${total_profit_profit}")
    else:
        st.write("No items selected.")

    # Menampilkan hasil greedy by density
    st.subheader("Selected Items by Density")
    if selected_items_density:
        selected_data_density = {
            "Name": [item['name'] for item in selected_items_density],
            "Weight": [item['weight'] for item in selected_items_density],
            "Profit": [item['profit'] for item in selected_items_density]
        }
        st.table(selected_data_density)
        st.write(f"Total Weight: {total_weight_density} kg")
        st.write(f"Total Profit: ${total_profit_density}")
    else:
        st.write("No items selected.")
    

st.subheader("The Best Option")
profmax = 0
best_items = []

if total_profit_weight > profmax:
        profmax = total_profit_weight
        best_items = selected_items_weight
if total_profit_profit > profmax:
        profmax = total_profit_profit
        best_items = selected_items_profit
if total_profit_density > profmax:
        profmax = total_profit_density
        best_items = selected_items_density

if best_items:
        best_data = {
            "Name": [item['name'] for item in best_items],
            "Weight": [item['weight'] for item in best_items],
            "Profit": [item['profit'] for item in best_items]
        }
        st.table(best_data)
        st.write(f"Total Weight: {sum(item['weight'] for item in best_items)} kg")
        st.write(f"Total Profit: ${profmax}")
else:
        st.write("No items selected.")



from itertools import combinations

# Function to calculate total value and weight of a given combination
def calculate_value_weight(combination, val, wt):
    total_value = sum(val[i] for i in combination)
    total_weight = sum(wt[i] for i in combination)
    return total_value, total_weight

# Function to find all possible combinations of items and return the best one
def knapSackBruteForce(W, weights, profits, n, items):
    max_value = 0
    best_combination = []
    all_combinations = []

    # Check all possible combinations of items
    for r in range(n + 1):
        for combination in combinations(range(n), r):
            total_value, total_weight = calculate_value_weight(combination, profits, weights)
            comb_items = [items[i] for i in combination]
            all_combinations.append((comb_items, total_value, total_weight))
            if total_weight <= W and total_value > max_value:
                max_value = total_value
                best_combination = combination

    return max_value, best_combination, all_combinations

# Driver code
if __name__ == "__main__":
    # Get input from user
    # n = int(input("Enter number of items: "))

    # val = []
    # wt = []
    # items = []

    # for i in range(n):
    #     item_name = input(f"Enter name of item {i+1}: ")
    #     v = int(input(f"Enter value of item {i+1}: "))
    #     w = int(input(f"Enter weight of item {i+1}: "))
    #     items.append(item_name)
    #     val.append(v)
    #     wt.append(w)

    # W = int(input("Enter maximum weight capacity of the knapsack: "))

    # Find the best combination using brute force
    max_prof, best_combination, all_combinations = knapSackBruteForce(max_capacity, weights, profits, itemtotal, items)

    # Output all combinations
    print("\nAll possible combinations (item names, total value, total weight):")
    for comb_items, total_value, total_weight in all_combinations:
        print(f"Items: {comb_items}, Total Value: {total_value}, Total Weight: {total_weight}")

    # Output the maximum value and the best combination
    best_comb_items = [items[i] for i in best_combination]
    st.write(f"\nMaximum Profit that can we get = {max_prof}")
    st.write("Items included in the best combination:", best_comb_items)

    
    
    # st.subheader("The Best Option")
    # profmax=0
    # if total_profit_weight>profmax:
    #     profmax=total_profit_weight
    # if total_profit_profit>profmax:
    #     profmax=total_profit_profit
    # if total_profit_density>profmax:
    #     profmax=total_profit_density
    

    # #looking for the best item options
    # bestItems=""
    # if profmax==total_profit_density:
    #     bestItems=selected_items_density["Name"]
    # if profmax==total_profit_weight:
    #     bestItems=selected_items_weight["Name"]
    # if profmax==total_profit_profit:
    #     bestItems=selected_items_profit["Name"]

    

    
    # st.write(f"The maximum profit that can we get {profmax}")
    # st.write(f"The items that you should take : {bestItems}")
        

