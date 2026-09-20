from fastapi import FastAPI, Form
import json

app = FastAPI()


@app.post("/submit")
async def submit(
    name: str = Form(...),
    father: str = Form(...),
    motherName: str = Form(...),
    gender: str = Form(...),
    dob: str = Form(...),
    email: str = Form(...),
    level: str = Form(...),
    department: str = Form(...),
    phone: str = Form(...)
):

    student = {
        "name": name,
        "father": father,
        "motherName": motherName,
        "gender": gender,
        "dob": dob,
        "email": email,
        "level": level,
        "department": department,
        "phone": phone
    }

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    return {
        "message": "Student submitted successfully",
        "student": student
    }