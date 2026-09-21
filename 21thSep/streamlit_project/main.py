import streamlit as st


st.title("hello App")
st.subheader("This is the subheader of the streamlit")

st.text("Welcome to your first interactive app")

st.write("Choose your fav. variety of app")



sb =st.selectbox("Select your favorite subject", ["CAO", "C++", "Networking", "Java"]) 




if st.button("submit"):
    st.success("Your details have been saved ")

cb=st.checkbox("I agree with the terms and the conditions")

gender_type= st.radio("Choose your Gender", ["Male","Female","others" ])

st.write(f"Selected Gender is {gender_type}") #f is for formatted string

value= st.slider("Form satisfication", 0, 5, 10)



