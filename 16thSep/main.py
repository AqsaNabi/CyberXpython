from fastapi import FastAPI, Path
import json
app =FastAPI()
@app.get("/")
def hey():
    return {'message':'Patient Management System API'}
@app.get('/about')
def about():
    return{'message':'A fully functional API to manage your patient records'}
def load_data():
    with open('patients.json', 'r') as f:
         data=json.load(f)

    return data
@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patient/{pat_id}')
def view_patient(pat_id: str= Path(..., description='OID of the patients are required', example='P001')):
    data=load_data()
    if pat_id in data:
        return data[pat_id]
    return {'error': 'Patient not found'}

    
