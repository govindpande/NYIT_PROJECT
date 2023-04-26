import pandas as pd
import ydata_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report



@st.cache
def get_data():
  # return pd.read_csv("http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv")
  return pd.read_csv('data/financial1.csv')




def main():
  df = get_data()

  ################################ SIDEBAR ################################

  st.sidebar.header("Final Project for MS")

  st.sidebar.markdown(" ")
  st.sidebar.markdown("*This project is done as a part of the final project for the MS in Data Science")

  pr = df.profile_report()

  st_profile_report(pr)


main()
