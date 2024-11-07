import streamlit as st

st.title("🎈GitBot")
st.write(
    "App to search the commit history"
)

# Create a selectbox (dropdown) with options
selected_option = st.selectbox(
    'Choose a repository:',
    # ['Red', 'Green', 'Blue', 'Yellow']
)

