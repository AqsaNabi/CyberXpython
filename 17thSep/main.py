from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated
class AAddress(BaseModel):
    city: str
    state: str
    pin: str

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
    height: float
    address: AAddress # is a complex data model which will have its own other field, we can create a nested model 



    @computed_field
    @property 
    def calculated_bmi(self)-> float:
        bmi =round(self.height/(self.weight**2), 2)
        return bmi

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
    @model_validator(mode='after')
    def validate_emergency_contacts(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emerrgency contact')
        return model
         

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
    print('BMI', patient.calculated_bmi)
    
    

def update_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print("data updated")



Add_dict={'city': 'srinagar', 'state':'kashmir', 'pin':'190003'}

add1= AAddress(**Add_dict)



patient_info={'name': 'aqsa', 'age':'70','height':183 ,'weight': 88.9, 'married': True, 'contact_details': {'phone': 'XXXXXXXXX', 'emergency':'xxxxxxxx'}, 'email':'abc@hdfc.com', 'link':'https://example.com/bb/mk', 'address': add1}

p1=patient(**patient_info)
inst_data(p1)
print(p1)
print(p1.address.pin)
temp =p1.model_dump(include=['name'])    
temp2 =p1.model_dump(exclude=['name'])  
print(temp)
print(type(temp))