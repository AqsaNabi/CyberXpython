import streamlit as st


st.title("Session State Basics")
# Initialization

"st.session_state object:", st.session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter']=0

if 'boolean' not in st.session_state:
    st.session_state.boolean=False


st.write(st.session_state)

st.write("a_counter is:", st.session_state["a_counter"])

st.write("boolean is:", st.session_state.boolean)



for the_key in st.session_state.keys():
    st.write(the_key)


for the_values in st.session_state.values():
    st.write(the_values)



#to clear session using del for a particular key
#del st.session_state[key]


#del all key pair of the session
for key in st.session_state.keys():
    del st.session_state[key]


    #connecting session state with a widget
   
   
level= st.slider("The level of the skills", 1,20, key="slider")

st.write(st.session_state)





#to clear session using del for a particular key
#del st.session_state[key]


#del all key pair of the session
for key in st.session_state.keys():
    del st.session_state[key]

