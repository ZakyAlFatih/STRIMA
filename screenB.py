import streamlit as st
import timeit
from itertools import combinations



# Your app code goes here
st.sidebar.title("Description")
st.sidebar.info(
    """
    **Jastiper Best Friend** is your go-to app for optimizing your shopping list.
    Whether you are trying to maximize profit or minimize weight, we provide the best 
    solutions using both greedy algorithms and brute force methods. Our app is designed 
    to help you make the best decisions effortlessly.
    """
)

st.sidebar.header("About Us")
st.sidebar.image("./images/aboutusfix_tubesStrima.png")



st.title("Jastiper Best Friend")


def calculate_value_weight(combination, val, wt):
    total_value = sum(val[i] for i in combination)
    total_weight = sum(wt[i] for i in combination)
    return total_value, total_weight

# Function to find all possible combinations of items and return the best one
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

# Gabungkan semua informasi barang dalam satu list
items_data = [{'name': items[i], 'weight': weights[i], 'profit': profits[i]} for i in range(itemtotal)]

# Measure execution time for greedy algorithms including the best option selection
def measure_greedy_time():
    selected_items_weight, total_weight_weight, total_profit_weight = greedy_algorithm(items_data, max_capacity, "weight")
    selected_items_profit, total_weight_profit, total_profit_profit = greedy_algorithm(items_data, max_capacity, "profit")
    selected_items_density, total_weight_density, total_profit_density = greedy_algorithm(items_data, max_capacity, "density")

    profmax = max(total_profit_weight, total_profit_profit, total_profit_density)
    if profmax == total_profit_weight:
        best_items = selected_items_weight
    elif profmax == total_profit_profit:
        best_items = selected_items_profit
    else:
        best_items = selected_items_density

    return best_items, profmax

if itemtotal > 0:
    greedy_execution_time = timeit.timeit(measure_greedy_time, number=1) * 1_000_000  # in microseconds
    
    
    # Get the best greedy solution
    best_items, profmax = measure_greedy_time()
    
    #Menampilkan greedy by weight
    

    # Display the best greedy solution
    st.subheader("The Best Option Based on Greedy Result")
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
    st.write(f"Execution time for Greedy algorithms: {greedy_execution_time:.2f} microseconds")
    
    # Measure execution time for brute force algorithm
    def measure_brute_force_time():
        knapSackBruteForce(max_capacity, weights, profits, itemtotal, items)
    
    brute_force_execution_time = timeit.timeit(measure_brute_force_time, number=1) * 1_000_000  # in microseconds
    

    # Brute force solution
    max_prof, best_combination, all_combinations = knapSackBruteForce(max_capacity, weights, profits, itemtotal, items)

    # Output all combinations
    st.subheader("Brute Force Way")
    all_combinations_data = {
        "Name": [", ".join(comb_items) for comb_items, _, _ in all_combinations],
        "Weight": [total_value for _, total_value, _ in all_combinations],
        "Profit": [total_weight for _, _, total_weight in all_combinations]
    }

    # Output all combinations as a table
    st.subheader("All Possible Combinations")
    st.table(all_combinations_data)

    # Output the maximum value and the best combination
    best_comb_items = [items[i] for i in best_combination]
    st.write(f"\nMaximum Profit that can we get : ${max_prof}")
    st.write(f"Total weight : {sum(weights[i] for i in best_combination)}")
    st.write("Items included in the best combination:")
    best_comb_data = {
        "Name": best_comb_items
    }
    st.table(best_comb_data)
    st.write(f"Execution time for Brute Force algorithm: {brute_force_execution_time:.2f} microseconds")

    #profmax = greedy
    #max_prof = brute force
    # best_items = greedy
    # best_comb_items = brute force
    
    if profmax > max_prof:
        best_option = profmax
        final_best_items = best_items 
        final_weight = sum(item['weight'] for item in best_items)
    else:
        best_option = max_prof
        final_best_items = best_comb_items
        final_weight = sum(weights[i] for i in best_combination)

    st.header("Best Option Between Greedy and Brute Force")
    final_best_data = {
        "Name": final_best_items,
        "Weight": [weights[items.index(name)] for name in final_best_items],
        "Profit": [profits[items.index(name)] for name in final_best_items]
    }
    st.table(final_best_data)
    st.write(f"Total Weight: {final_weight} kg")
    st.write(f"Maximum Profit: ${best_option}")

