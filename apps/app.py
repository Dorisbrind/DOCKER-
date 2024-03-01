import streamlit as st

def home():
    st.markdown('<h1 style="color: blue;">WELCOME TO MY FIRST STREAMLIT PAGE</h1>', unsafe_allow_html=True)
    st.write('Cette application Streamlit a deux pages.')

def do_this():
    st.markdown('<h1 style="color: green;">Do This</h1>', unsafe_allow_html=True)
    st.write('You can do whatever you want on this page.')

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home', 'Do This'])

    if selection == 'Home':
        home()
    elif selection == 'Do This':
        do_this()

if __name__ == "__main__":
    main()
