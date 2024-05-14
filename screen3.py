import streamlit as st

st.title("JASTIPER SOHIB ")

st.subheader("Insert the maximum capacity")
maxs=st.number_input("")
st.subheader("How many items that you want to input ?")
itemtotal=st.number_input("Enter an integer:", min_value=None, max_value=None, value=0)

items= []
weights= []
profits= []

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



if itemtotal > 0:
    max_capacity = maxs

    # Gabungkan semua informasi barang dalam satu list
    items_data = [{'name': items[i], 'weight': weights[i], 'profit': profits[i]} for i in range(itemtotal)]

    # Sortir barang berdasarkan berat dari yang terendah
    sorted_items = sorted(items_data, key=lambda x: x['weight'])

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

    st.subheader("Selected Items")
    if selected_items:
        selected_data = {
            "Name": [item['name'] for item in selected_items],
            "Weight": [item['weight'] for item in selected_items],
            "Profit": [item['profit'] for item in selected_items]
        }
        st.table(selected_data)
        st.write(f"Total Weight: {total_weight} kg")
        st.write(f"Total Profit: ${total_profit}")
    else:
        st.write("No items selected.")



# # Kapasitas maksimal ransel
# max_capacity = 20

# # Algoritma greedy berdasarkan berat
# def greedy_by_weight(items, max_capacity):
#     # Mengurutkan barang berdasarkan berat dari yang terendah
#     items = sorted(items, key=lambda x: x['weight'])
    
#     total_weight = 0
#     total_profit = 0
#     selected_items = []

#     for item in items:
#         if total_weight + item['weight'] <= max_capacity:
#             selected_items.append(item)
#             total_weight += item['weight']
#             total_profit += item['profit']
#         else:
#             break

#     return selected_items, total_weight, total_profit

# # Memanggil fungsi dan menampilkan hasil
# selected_items, total_weight, total_profit = greedy_by_weight(items, max_capacity)

# print("Barang yang dipilih:")
# for item in selected_items:
#     print(f"Barang {item['item']}: Berat = {item['weight']} kg, Profit = ${item['profit']}")

# print(f"\nTotal Berat: {total_weight} kg")
# print(f"Total Profit: ${total_profit}")
