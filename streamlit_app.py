import streamlit as st

st.title("🎈GitBot")
# st.markdown("JuggBot :juggernaut:")

# Create two columns
col1, col2 = st.columns(2)

# Display text in the first column
with col1:
    st.header("Header")
    # st.write("Here is some text next to the image. You can add more content here.")

# Display image in the second column
with col2:
    st.image("/workspaces/GitApp/jugg_image.png", caption="Cute Cat", width=300)  


st.write(
    "App to search the commit history"
)
# st.image('/workspaces/GitApp/jugg_image.png')

st.sidebar.title("Home")


# Create a selectbox (dropdown) with options
selected_option = st.sidebar.selectbox(
    'Choose a GitHub repository:',
    ['Red', 'Green', 'Blue', 'Yellow']
)

st.sidebar.selectbox("Pick one", ["cats", "dogs"])