import streamlit as st
import langchain_helper as lh
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("pick a cuisine",("India","Italian","Mexican"))

if cuisine:
    response=lh.generate_restaurant_name_items(cuisine)
    st.header(response["restaurant_name"].split())
    menu_items=response["menu_items"].split(",")
    st.write("***Menu Items***")
    for item in menu_items:
        st.write("-",item)
