import streamlit as st

ss = st.session_state
ss.foo = 5

st.write(ss)
