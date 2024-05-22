import streamlit as st
import time 
from itertools import combinations

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

def calculate_value_weight(combination, val, wt):
    total_value = sum(val[i] for i in combination)
    total_weight = sum(wt[i] for i in combination)
    return total_value, total_weight

def knapSackBruteForce(W, weights, profits, n, items):
    max_value = 0
    best_combination = []
    all_combinations = []

    for r in range(n + 1):
        for combination in combinations(range(n), r):
            total_value, total_weight = calculate_value_weight(combination, profits, weights)
            comb_items = [items[i] for i in combination]
            all_combinations.append((comb_items, total_value, total_weight))
            if total_weight <= W and total_value > max_value:
                max_value = total_value
                best_combination = combination

    return max_value, best_combination, all_combinations

#main program
if itemtotal > 0:
    
    # Gabungkan semua informasi barang dalam satu list
    items_data = [{'name': items[i], 'weight': weights[i], 'profit': profits[i]} for i in range(itemtotal)]
    #start greedy
    start_time = time.time()
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
    
    # Mencari opsi terbaik
    st.subheader("The Best Option")
    profmax = max(total_profit_weight, total_profit_profit, total_profit_density)

    if profmax == total_profit_weight:
        best_items = selected_items_weight
    elif profmax == total_profit_profit:
        best_items = selected_items_profit
    else:
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
    end_time = time.time()
    execution_time = end_time - start_time
    st.write(f"Execution time: {execution_time} seconds")
    #brute force
    start_time = time.time()
    # Brute force solution
    max_prof, best_combination, all_combinations = knapSackBruteForce(max_capacity, weights, profits, itemtotal, items)

    # Output all combinations
    st.subheader("Brute Force Way")
    #st.write("\nAll possible combinations (item names, total value, total weight):")
    all_combinations_data = {
        "Items": [", ".join(comb_items) for comb_items, _, _ in all_combinations],
        "Total Value": [total_value for _, total_value, _ in all_combinations],
        "Total Weight": [total_weight for _, _, total_weight in all_combinations]
    }

    # Output all combinations as a table
    st.subheader("All Possible Combinations")
    st.table(all_combinations_data)

    # Output the maximum value and the best combination
    best_comb_items = [items[i] for i in best_combination]
    st.write(f"\nMaximum Profit that can we get = {max_prof}")
    st.write("Items included in the best combination:")
    best_comb_data = {
        "Name": best_comb_items
    }
    st.table(best_comb_data)
    end_time = time.time()
    execution_time = end_time - start_time
    st.write(f"Execution time: {execution_time} seconds")