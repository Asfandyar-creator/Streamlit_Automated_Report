import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport


from streamlit_pandas_profiling import st_profile_report


df = pd.read_csv('car data.csv')
prof = ProfileReport(df)
st_profile_report(prof)