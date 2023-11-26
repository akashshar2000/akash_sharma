import streamlit as st

data1=st.text_input("enter  your name:")
fname=st.text_input("enter your father name:")
adr=st.text_area("enter your address:")
classdata=st.selectbox("enter your class:",(1,2,3,4))

button=st.button("Submit")
if button:
    st.markdown("""
    name:{name}
    father name:{fname}
    address:{adr}
    class:{classdata}
""")
