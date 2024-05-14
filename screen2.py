import streamlit as st

# Title and Text Block
st.title('Hasil CatCulate')
st.text('Greedy by Density')

# Create Columns for Left and Right sections
col1, col2 = st.columns(2)

# Left Column - Input data
with col1:
  # Text Block for Input section
  st.subheader('List Barang')
  # Input fields for Barang Nama, Berat Barang
  nama_barang = st.text_input('Nama Barang')
  berat_barang = st.number_input('Berat Barang')
  # Button to Tambah Barang
  tambah_barang = st.button('Tambah Barang')

  # Display selected Barang
  st.subheader('Barang Terpilih')
  # Table to show Barang Nama, Jumlah, Profit
  data = [['Album A', 2, 240000], ['Album B', 5, 500000], ['Keychain F', 7, 210000], ['Tas brand C', 1, 180000], ['Snack E', 13, 130000], ['Boneka D', 2, 180000]]
  table = st.table(data)

  # Calculate Total Berat and Profit
  total_berat = sum(item[1] for item in data)
  total_profit = sum(item[2] for item in data)

  # Display Total Berat and Profit
  st.subheader('Total')
  st.write('Total Berat:', total_berat, 'Kg')
  st.write('Total Profit:', total_profit, 'Rp')

# Right Column - Display Information
with col2:
  # Text Block for Hasil CatCulate
  st.subheader('Batas Maksimum Bagasi (Kg)')
  # Input field for Batas Maksimum Bagasi
  batas_maksimum_bagasi = st.number_input('Batas Maksimum Bagasi')
  # Text Block for Perhitungan
  st.subheader('Keuntungan (Rp)')

  # Button to Mulai Hitung
  mulai_hitung = st.button('Mulai Hitung')

# Functionality based on button clicks (placeholder for now)
if tambah_barang:
  st.write('Barang added!')

if mulai_hitung:
  st.write('Calculation started!')

