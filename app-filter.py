import streamlit as st
import pandas as pd

st.title('Streamlit - search ranges')
DATA_URL = 'dataset.csv'


@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)

    return data


@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filter_data_bysex = data[data['Sex'] == sex]

    return filter_data_bysex


data = load_data()
selected_sex = st.selectbox('Select Sex', data['sex'].unique())
btnFilterbySex = st.button('Filter by Sex')

# startid = st.text_input('Start index : ')
# endid = st.text_input('End index : ')
# btnRange = st.button(' Search by range ')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f'Total items : {count_row} rows')

    st.dataframe(filterbysex)
