import streamlit as st

st.title("🎈GitBot")
st.write(
    "App to search the commit history"
)

st.sidebar.title("Sidebar")


# Create a selectbox (dropdown) with options
selected_option = st.sidebar.selectbox(
    'Choose a repository:',
    ['Red', 'Green', 'Blue', 'Yellow']
)

