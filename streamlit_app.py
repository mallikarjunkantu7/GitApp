import streamlit as st

st.title("🎈GitBot")
st.write(
    "App to search the commit history"
)

# Create a selectbox (dropdown) with options
selected_option = st.selectbox(
    'Choose a color:',
    ['Red', 'Green', 'Blue', 'Yellow']
)

# Display the selected option
st.write(f'You selected: {selected_option}')