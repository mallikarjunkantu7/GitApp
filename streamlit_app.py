import streamlit as st

st.title("🎈GitBot")
st.markdown("JuggBit : juggernaut")
st.write(
    "App to search the commit history"
)
st.image('/workspaces/GitApp/jugg_image.png')

st.sidebar.title("Home")


# Create a selectbox (dropdown) with options
selected_option = st.sidebar.selectbox(
    'Choose a GitHub repository:',
    ['Red', 'Green', 'Blue', 'Yellow']
)

st.sidebar.selectbox("Pick one", ["cats", "dogs"])