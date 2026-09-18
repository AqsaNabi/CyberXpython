from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json


app =FastAPI()
class Patient(BaseModel):
    id: Annotated[str, Field(...,description='Id of the patient' , examples=['P001'])]
    name: Annotated[str, Field(...,description='Name of the patient' , examples=['Ram'])]
    city: Annotated[str, Field(...,description='City where the patient is from' , examples=['Srinagar'])]
    age: Annotated[int, Field(...,description='Age of the patient' , gt=0, lt=100)] 
    gender: Annotated[Literal['male', 'female', 'others'], Field(...,description='gender of the patient' )]
    height: Annotated[float, Field(...,description='Height of the patient' , gt=0)] 
    weight: Annotated[float, Field(...,description='Weight of the patient' , gt=0)] 


    @computed_field
    @property

    def bmi(self)-> float:
        bmi= round(self.weight/(self.height**2), 2)
        return bmi

    @computed_field
    @property

    def verdict(self)->str:
        if self.bmi<18.5:
            return 'underrweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
                    return 'Normal'
        else:
             return 'Obese'

def load_data():
    with open('patients.json', 'r') as f:
        data =json.load(f)

    return data

def save_data(data):
     with open('patients.json', 'w') as f:
          json.dump(data, f)

@app.get("/")
def hey():
    return {'message':'Patient Management System API'}
@app.get('/about')
def about():
    return{'message':'A fully functional API to manage your patient records'} 
@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patient/{pat_id}')
def view_patient(pat_id: str= Path(..., description='OID of the patients are required', example='P001')):
    data=load_data()
    if pat_id in data:
        return data[pat_id]
    raise HTTPException(status_code=404, detail="Patient not found")   
@app.get('/sort')
def sort_patients(sort_by:str=Query(..., description='on the basis of height weight or bmi'), order: str=Query('asc', description='sort in asc or desc order')):
    valid_fields= ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid field seclect from {valid_fields}')
    if order not in['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select asc and desc')
    data =load_data()
    
    sort_order= True if order =='desc' else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data 

@app.post('/create')
def create_patient(patient:Patient): #here it is an pydantic object
     #validated data is in now object of create_patient rather than doing it manually
    #load data
    data=load_data()#python dictionary
    # check if the patient already exists
    if patient.id in data:
         raise HTTPException(status_code=400, detail='Patient already exists')
    data[patient.id]=patient.model_dump(exclude=['id'])

    #save this data into json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient created successgully'}) 