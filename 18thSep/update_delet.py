from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional, Literal
import json


app =FastAPI()
class Patient(BaseModel):
    id: Annotated[str, Field(...,description='Id of the patient' , examples=['P001'])]
    name: Annotated[str, Field(...,description='Name of the patient' , examples=['Ram'])]
    city: Annotated[str, Field(...,description='City where the patient is from' , examples=['Srinagar'])]
    age: Annotated[int, Field(...,description='Age of the patient' , gt=0, lt=101)] 
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

class PatientUpdate(BaseModel):
     name: Annotated[Optional[str], Field(default=None)]
     city: Annotated[Optional[str], Field(default=None)]
     age: Annotated[Optional[int], Field(default=None)] 
     gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None )]
     height: Annotated[Optional[float], Field(default=None , gt=0)] 
     weight: Annotated[Optional[float], Field(default=None, gt=0)] 


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
@app.put('/edit/{patient_id}')

def update_patient(patient_id:str, patient_update: PatientUpdate):
    data =load_data()
    if patient_id not in data:
          raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient_info= data[patient_id]
    updated_patient_info=patient_update.model_dump(exclude_unset=True)
    for key, value in updated_patient_info.items():
          existing_patient_info[key]=value
    existing_patient_info['id']=patient_id 
    patient_pydantic_obj=Patient(**existing_patient_info)   
    existing_patient_info=patient_pydantic_obj.model_dump(exclude='id')
    data[patient_id]=existing_patient_info
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient updated'} )
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
@app.delete('/delete/{patient_id}') 
def delete_patient(patient_id:str):
     data=load_data()

     if patient_id not in data:
          raise HTTPException(status_code=404, detail='Patient not found')

     del data[patient_id]
     save_data(data)

     return JSONResponse(status_code=200, content={'message': 'patient deleted'})