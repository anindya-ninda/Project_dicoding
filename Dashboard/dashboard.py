import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


st.title('Proyek Analisis Data - Bike Share')
st.write('Nama: Anindya Rahima')
st.write('Email: anindya.ninda.rahima@gmail.com')
st.write('ID Dicoding: anindya_rahima')


tab1, tab2, tab3 = st.tabs(["Wrangling Data", "Exploratory Data Analysis (EDA)", "Visualization & Explanatory Analysis"])
 
with tab1:
    st.subheader("Wrangling Data")
    code = """day_df = pd.read_csv("day.csv", delimiter=",")")"""
    st.code(code, language='python')
    
    code = """hour_df = pd.read_csv("hour.csv", delimiter=",")")"""
    st.code(code, language='python')

    code = """hour_df.head()"""
    st.code(code, language='python')

    code = """day_df.head()"""
    st.code(code, language='python')

    st.subheader("Assessing Data")
    code = """day_df.info()"""
    st.code(code, language='python')

    code = """hour_df.isnull().sum()"""
    st.code(code, language='python')

    code = """day_df.isnull().sum()"""
    st.code(code, language='python')

    code = """day_df.duplicated().sum()"""
    st.code(code, language='python')

    code = """hour_df.duplicated().sum()"""
    st.code(code, language='python')

    code = """day_df.describe()"""
    st.code(code, language='python')

    code = """hour_df.describe()"""
    st.code(code, language='python')

    st.subheader('Cleaning Data')
    code = """datetime_columns = ["dteday"]
        for column in datetime_columns:
        day_df[column] = pd.to_datetime(day_df[column])"""
    st.code(code, language='python')

    code = """day_df.info()"""
    st.code(code, language='python')

    code = """df = pd.read_csv("hour.csv")
         df.drop_duplicates(inplace=True)"""
    st.code(code, language='python')

    code = """df = pd.read_csv("day.csv")
    df.drop_duplicates(inplace=True)"""
    st.code(code, language='python')
 


with tab2:
    st.header("Exploratory Data Analysis (EDA)")
    code = """day_df.describe()"""
    st.code(code, language = 'python')

    code = """hour_df.describe()"""
    st.code(code, language = 'python')

 
with tab3:
    st.header("Visualization & Explanatory Analysis")
    st.subheader('1. Bagaimana demografi total peminjaman sepeda berdasarkan cuaca?')

    code = """byweather_df = day_df.groupby(by="weathersit").cnt.sum().reset_index()
    byweather_df.weathersit.replace(1, "Clear", inplace=True)
    byweather_df.weathersit.replace(2, "Cloudy", inplace=True)
    byweather_df.weathersit.replace(3, "Light rain", inplace=True)
    byweather_df.weathersit.replace(4, "Heavy rain", inplace=True)

    byweather_df.rename(columns={
    "weathersit": "Weather",
    "cnt": "Total_user"
    }, inplace=True)

    byweather_df"""
    st.code(code, language = 'python')

    plt.figure(figsize=(10, 4))
 
    sns.barplot(
    y="Weather", 
    x="Total_user",
    data=byweather_df.sort_values(by="Total_user", ascending=False)
    )
    plt.title("Total Sharing by Weather", loc="center", fontsize=15)
    plt.xlabel("Average sharing")
    plt.ylabel("Weather")

    st.subheader('Apa yang dapat memengaruhi pesepeda agar lebih sering bersepeda?')
    code = """day_df = pd.read_csv('day.csv')"""
    st.code(code, language = 'python')

    code = """day_df.head()"""
    st.code(code, language = 'python')

    code = """fix_df = day_df.groupby(by="dteday").cnt.sum()"""
    st.code(code, language = 'python')

    code = """import statsmodels.api as sm"""
    st.code(code, language = 'python')

    code = """day_df.head()"""
    st.code(code, language = 'python')

    code = """day_df.corr()['cnt']"""
    st.code(code, language = 'python')

    code = """day_df.columns"""
    st.code(code, language = 'python')

    code = """X = day_df[['temp','atemp']]
    Y = day_df['cnt']"""
    st.code(code, language = 'python')

    code = """X = sm.add_constant(X)
    reg_res = sm.OLS(Y,X).fit()
    reg_res.summary()"""
    st.code(code, language = 'python')

    code = """alpha = reg_res.params['const']
    print('The constant term for the regression line is ' +str(round(alpha,2)))"""
    st.code(code, language = 'python')

    code = """beta1 = reg_res.params['temp'] 
    print('We predict that one additional temp charges the user by' +str(round(beta1,3)))"""
    st.code(code, language = 'python')

    code = """beta2 = reg_res.params['atemp'] 
    print('We predict that one additional atemp charges the user by' +str(round(beta2,3)))"""
    st.code(code, language = 'python')

    code = """r_sqrd = reg_res.rsquared
    print('Temp and Atemp ' +str(round(100*r_sqrd,1)) + '% of the variation in user')"""
    st.code(code, language = 'python')

    code = """temp_max = day_df['temp'].max()
    atemp_max = day_df['atemp'].max()

    reg_res.predict([1, temp_max, atemp_max])"""
    st.code(code, language = 'python')

    code = """temp_min = day_df['temp'].min()
    atemp_min = day_df['atemp'].min()

    reg_res.predict([1, temp_min, atemp_min])"""
    st.code(code, language = 'python')

    code = """pred = reg_res.predict(X)
    day_df['pred_cnt'] = pred
    day_df.head()"""
    st.code(code, language = 'python')

    code = """sum(day_df['cnt'] - day_df['pred_cnt'])"""
    st.code(code, language = 'python')

    fig, ax = plt.subplots()

    ax.scatter(day_df['temp'], day_df['cnt'])
    ax.plot(day_df['temp'], day_df['pred_cnt'], color = 'black')

    ax.set_ylabel('cnt', fontsize = 14)
    ax.set_xlabel('temp', fontsize = 14)
    plt.show()




    
