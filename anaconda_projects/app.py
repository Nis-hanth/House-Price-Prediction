import streamlit as st
import pandas as pd
import numpy as np
import pickle



import streamlit as st

st.title("My First App")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}")
