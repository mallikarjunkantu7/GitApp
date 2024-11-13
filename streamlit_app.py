import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# st.title("GitBot")
# # st.markdown("JuggBot :juggernaut:")


# st.write(
#     "OnePlace to search the GITHUB commit history"
# )

# st.image('/workspaces/GitApp/jugg_image.png')

# st.sidebar.title("Home")


# # Create a selectbox (dropdown) with options
# selected_option = st.sidebar.selectbox(
#     'Choose a GitHub repository:',
#     ['Red', 'Green', 'Blue', 'Yellow']
# )

def run():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.write("# Juggernaut Bot👋")
    # st.image('jugg_image.jpg')

    st.write(""" "OnePlace to search the GITHUB commit history"         
             """)


if __name__ == "__main__":
    run()

