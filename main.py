import streamlit as st

col1, col2 = st.columns([2,3])

with col1:
    st.title('here is column1')
    st.subheader('i am column1 subheader')

with col2:
    st.title('here is column2')
    st.checkbox('this is checkbox2 in col2', key='checkbox2_1')
    st.checkbox('this is checkbox2 in col2', key='checkbox2_2')
