import streamlit as st
import numpy as np
import pandas as pd
import timeit

ss = st.session_state

start = timeit.default_timer()
rows = st.number_input("how many rows", 0)


def make_df(rows):
    dates = pd.date_range("20130101", periods=rows)
    df = pd.DataFrame(np.random.randn(rows, 4), index=dates, columns=list("ABCD"))
    return df


df = make_df(rows)
ss[rows] = df
st.write(df)
end = timeit.default_timer()
st.write(end - start)
