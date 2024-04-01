import streamlit as st
import os
import sys
import pandas as pd


def calculate(parameter, x_loc, y_loc, df_x, df_y):
    x = df_x[parameter].loc[x_loc] #[3]
    y = df_y['Mesurée'][y_loc-2]
    x_y = abs(x-y)
    return pd.DataFrame([{
        "parameter": parameter,
        "data": x,
        "Mesurée": y,
        "abs_difference": x_y
    }])
    
def main():
    st.title("CSV and XLSX Files Upload")
    uploaded_csv = st.file_uploader("Choose a CSV file", type='csv')
    uploaded_xlsx = st.file_uploader("Choose a XSLX file", type='xlsx')
    
    if uploaded_csv is not None:
        df_x = pd.read_csv(uploaded_csv)
        st.write("---------------------")
        st.subheader("About CSV")
        st.write(df_x)      
        
    if uploaded_xlsx is not None:
        df_y = pd.read_excel(uploaded_xlsx, engine='openpyxl')
        st.write("---------------------")
        st.subheader("About CSV")
        st.write(df_y)
        
    if uploaded_csv and uploaded_xlsx:
        df = pd.concat([calculate(parameter='1:Bat Ear Anode', x_loc=3, y_loc=10, df_x= df_x, df_y= df_y),
        calculate(parameter='1:Bat Ear Anode', x_loc=3, y_loc=50, df_x= df_x, df_y= df_y),
        calculate(parameter='1:AN Tab Sealant Pouch', x_loc=3, y_loc=14, df_x= df_x, df_y= df_y),
        calculate(parameter='1:AN TAB SEALANT', x_loc=3, y_loc=18, df_x= df_x, df_y= df_y),
        calculate(parameter='1:QR CODE X', x_loc=3, y_loc=22, df_x= df_x, df_y= df_y),
        calculate(parameter='1:QR CODE Y', x_loc=3, y_loc=24, df_x= df_x, df_y= df_y),
        calculate(parameter='1:ANGLE ANODE TAB SEALANT', x_loc=3, y_loc=26, df_x= df_x, df_y= df_y),
        calculate(parameter='1:Tape 1 Anode', x_loc=3, y_loc=30, df_x= df_x, df_y= df_y),
        calculate(parameter='1:Tape 2 Anode', x_loc=3, y_loc=32, df_x= df_x, df_y= df_y),
        calculate(parameter='1:TC beloz anode TAB', x_loc=3, y_loc=46, df_x= df_x, df_y= df_y),
        calculate(parameter='2:TAPE 3', x_loc=3, y_loc=34, df_x= df_x, df_y= df_y),
        calculate(parameter='2:TAPE 4', x_loc=3, y_loc=36, df_x= df_x, df_y= df_y),
        calculate(parameter='2:TAPE 5', x_loc=3, y_loc=38, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Bat Ear Cathode', x_loc=3, y_loc=12, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Bat Ear Cathode', x_loc=3, y_loc=52, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Cathode Tab Sealant Pouch', x_loc=3, y_loc=16, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Cathode Tab Sealant', x_loc=3, y_loc=20, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Angle cathode tab sealant', x_loc=3, y_loc=28, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Tape 6 Cathode', x_loc=3, y_loc=40, df_x= df_x, df_y= df_y),
        calculate(parameter='3:Tape 7 Cathode', x_loc=3, y_loc=42, df_x= df_x, df_y= df_y),
        calculate(parameter='3:TC Below Cathode Tab', x_loc=3, y_loc=48, df_x= df_x, df_y= df_y)])
        st.write("---------------------")
        st.subheader("RESULTS")
        st.write(df)

if __name__ == "__main__":
    main()