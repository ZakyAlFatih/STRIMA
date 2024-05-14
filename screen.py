import streamlit as st

st.title("Ini titless")
st.text("sdssdsdsds")

nama=st.text_input("Masukan nama","nama anda")
Nim=st.text_input("Masukan Nim","NIm")


if nama:
    st.text("Nama:"+nama)

    if len(Nim)<10:
        st.text("Nim:"+Nim)
    else:
      st.text("error")
    
    inikotak=st.selectbox('Pilih Jurusan',['RPL','DS','IF'])
    st.write(inikotak)
    Umur=st.slider("Umur",1,99)
    st.write(Umur)
    Gender=st.radio('Gender',['Pria','Wanita'])
    
    if Gender=="Pria":
       st.write("Selamat Datang Bapak",nama)
    else:
       st.write("Selamat Datang Ibu",nama)
    st.write(Gender)

    list_hobi=st.text_area("Hobi",'Main bola')
    list_hobi=[x.strip() for x in list_hobi.split(',')]

    st.write(list_hobi)

    st.image('https://dibimbing-cdn.sgp1.cdn.digitaloceanspaces.com/1666065647668-image%20(10).png.webp',caption="Kasian cuyy")

    st.markdown('[ini link ke bing](https://dibimbing-cdn.sgp1.cdn.digitaloceanspaces.com/1666065647668-image%20(10).png.webp)')


    import pandas as pd

    data={'Pekerjaan': ['Programmer','Dokter','Pengacara'],
          'Tier':['E','SS','A']}
    df=pd.DataFrame(data)

    st.dataframe(df)

    st.title("Buka Data")
    file=st.file_uploader('Pilih file jpg',type=['jpg','csv'])

    if file is not None:
        st.write(file.type)
        if file.type=="image/jpeg":
            st.image(file)
        else:
            data=pd.read_csv(file)

            st.dataframe(data)
    
    st.title("Kalkulator")

    angka1=st.number_input("Masukan angka 1",value=0)
    angka2=st.number_input("Masukan angka 2",value=0)

    operasi=st.radio('Pilih Operasi',["Penjumlahan (+)","Pengurangan (-)","Perkalian (*)","Pembagian (/)"])

    if st.button('hitung'):
        if operasi=="Penjumlahan (+)":
            hasil=angka1+angka2
        elif operasi == "Pengurangan (-)":
            hasil=angka1-angka2
        elif operasi== "Perkalian (*)":
            hasl=angka1*angka2
        elif operasi ==" Pembagian (/)":
            hasil=angka1/angka2
        
        st.success(f'Hasil {operasi}:{hasil}')
    
    st.sidebar.header('fitur kiri')

    if st.sidebar.checkbox('Biodata'):
        st.sidebar.write(f'Nama : {nama} ')
        
