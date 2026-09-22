import streamlit as st
from datetime import date
import pandas as pd
import requests



st.title("hello App")
st.subheader("This is the subheader of the streamlit")

st.text("Welcome to your first interactive app")

st.write("Choose your fav. variety of app")


name= st.text_input("Enter your name")


if name:
    st.write(f"Welcome {name} to the streamlit")

sb =st.selectbox("Select your favorite subject", ["CAO", "C++", "Networking", "Java"]) 




if st.button("submit"):
    st.success("Your details have been saved ")

cb=st.checkbox("I agree with the terms and the conditions")

gender_type= st.radio("Choose your Gender", ["Male","Female","others" ])

st.write(f"Selected Gender is {gender_type}") #f is for formatted string

value_slider= st.slider("Form satisfication", 0, 10, 5) #start, end, default value


st.write(f"Selected slider value is {value_slider}") #f is for formatted string


#uncrontollable output


st.number_input("The number of years of experience are", min_value=2, max_value=20, step=2)

#pure text input

dob=st.date_input("Enter you date of birth", min_value=date(1999,1,1),  max_value=date(2026,9,20))

if dob:
    integern=2026 - dob.year
    st.write(f"Your age is {integern}") 

#layouts in streamlit


#column divides
col1,col2=st.columns(2)

with col1:
    st.header("LEFT")
    st.image("https://tse4.mm.bing.net/th/id/OIP.TLe-J_yvllZadhsKlpcJDAHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", width=200)
    v1= st.button("you are on the left side")
   
    pass
with col2:
    st.header("RIGHT")
    st.image("https://static.vecteezy.com/system/resources/thumbnails/057/162/872/small_2x/adorable-baby-panda-cub-eating-bamboo-on-a-tree-branch-in-a-lush-green-forest-habitat-photo.jpeg", width=200)
    v1= st.button("you are on the right side")




menu=st.sidebar.write("Menu")
select_Device= st.sidebar.selectbox("Select Operating System", ['Mac','Windows', 'Ubuntu', 'linux' ])
other_options=st.sidebar.write("Other-options")


with st.expander("Terms and Conditions"):
    st.write("Person must follow the rules and regulations of the company, the concerning person should not use the company network for there personal use.")

st.markdown('### hello')
st.markdown('## hello')
st.markdown('> heyyyy')


#file=st.file_uploader("Upload your csv file", type=["csv"])
file="student.csv"
if file:
    df=pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)

if file:
    st.subheader("discription of the file")
    st.write(df.describe())

if file:
    course= df["Course"].unique()
    st.selectbox("Filter by unique courses", course)




