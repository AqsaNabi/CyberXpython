from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):
    #type validation
    name:str= Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', example=['Mehar','Salif'])]
    email: EmailStr 
    age:int= Field(gt=0, lt=100)
    weight: float= Field(gt=0) #greaterthan 0
    married: bool =False
    allergies: Annotated[Optional[list[str]], Field(default=None, max_length=5)]#to validate the data within the list
    contact_details: Dict[str, str]
    link:AnyUrl

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains=['hdfc.com','icici.com']

        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
    @field_validator('name', mode='after')
    @classmethod  
    def transform_name(cls,value):
        return value.upper()
    

def inst_data(patient: patient):
    print(patient.name)
    print(patient.age)
    
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.weight)
    print(patient.married)
    print(patient.email)
    print(patient.link)
    print("data installed")
   


    

def update_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("data updated")


patient_info={'name': 'aqsa', 'age':'70', 'weight': 88.9, 'married': True, 'contact_details': {'phone': 'XXXXXXXXX'}, 'email':'abc@hdfc.com', 'link':'https://example.com/bb/mk'}

p1=patient(**patient_info)


inst_data(p1)

        
