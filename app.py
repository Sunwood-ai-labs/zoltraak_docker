import streamlit as st


def load_markdown(file_path):
    with open(file_path, encoding="utf8") as f:
        return f.read()

def display_front_page():
    html_front = load_markdown('docs/page_front.md')
    st.markdown(f"{html_front}", unsafe_allow_html=True)
    
if __name__ == "__main__":
    display_front_page()
    x = st.slider('Select a value')
    st.write(x, 'squared is', x * x)