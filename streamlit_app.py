import streamlit as st

st.title("🎈GitBot")
st.write(
    "App to search the commit history"
)

st.sidebar.title("Home")


# Create a selectbox (dropdown) with options
selected_option = st.sidebar.selectbox(
    'Choose a GitHub repository:',
    ['Red', 'Green', 'Blue', 'Yellow']
)

st.selectbox("Pick one", ["cats", "dogs"])