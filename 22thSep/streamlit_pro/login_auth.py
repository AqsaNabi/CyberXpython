import streamlit as st

def load_data():
    with open('passs.json', 'r') as f:
        data =json.load(f)


"""def creds_enter():
    for items in load_data().values:
      if st.session_state["name"]==user and st.session_state["password"]==passwd:
        return true
      else:
        return false  


def authenticate_user():
    st.text_input(label="Username: ", value="", key="user", on_change=creds_enter)
    st.text_input(label="Password: ", value="", key="passwd", type="password",on_change=creds_enter)

    return false
if authenticate_user():    
    pass"""
