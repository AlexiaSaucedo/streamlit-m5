import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [25.61, -100.26],
    columns=['lat', 'lon'])

st.map(map_data)
st.dataframe(map_data)
