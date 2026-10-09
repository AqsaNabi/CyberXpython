# Talent Management System (TMS)

<p align="center">
  <strong>A Full-Stack Employee Management Application</strong>
  <br>
  Built with Python, FastAPI, and Streamlit
</p>

---

## 📌 Overview

As a team, we developed the **Talent Management System (TMS)** to simplify employee management and daily workplace operations. Our goal was to create a lightweight, user-friendly application that allows employees to manage attendance, apply for leave, and access their personal information through a single platform.

We worked together to build a full-stack application using **FastAPI** for the backend and **Streamlit** for the frontend. We used JSON files for data persistence, JWT-based authentication for login, and a location verification step to support workplace attendance checks.

Our project combines the following components:

<ul>
  <li>A <strong>FastAPI backend</strong> for API-driven operations.</li>
  <li>A <strong>Streamlit frontend</strong> for employee interaction.</li>
  <li><strong>JSON-based storage</strong> for employee, attendance, leave, and personal detail records.</li>
  <li><strong>JWT authentication</strong> to support authenticated sessions.</li>
  <li><strong>Location verification</strong> as part of the attendance check-in workflow.</li>
</ul>

## ✨ Key Features

### 1. Employee Registration

We developed a registration module that collects employee personal and contact details.

<ul>
  <li>Employee account creation.</li>
  <li>Email uniqueness validation.</li>
  <li>Storage of registration records in JSON files.</li>
</ul>

### 2. Employee Login and Authentication

We implemented a login system that validates employee credentials through the backend.

<ul>
  <li>Email and password-based login.</li>
  <li>Credential validation using stored employee records.</li>
  <li>JWT generation after successful authentication.</li>
</ul>

### 3. Attendance Management

We developed attendance functionality to help employees track their daily work activities.

<ul>
  <li>Employee check-in and check-out.</li>
  <li>Break start and resume functionality.</li>
  <li>Attendance timestamps and working-hour summaries.</li>
  <li>Persistent attendance records in JSON storage.</li>
</ul>

### 4. Leave Management

We implemented a leave management module through which employees can submit leave applications.

<ul>
  <li>Single-day and multiple-day leave applications.</li>
  <li>Leave start date and end date selection.</li>
  <li>Reason for leave.</li>
  <li>Storage and retrieval of leave history.</li>
</ul>

### 5. Employee Details

We created a personal details section where employees can view their stored information through the dashboard.

### 6. Location-Based Check-In

We integrated a location verification step into the attendance workflow to support workplace attendance checks based on the configured location.

### 7. Interactive Dashboard

We built the user interface with Streamlit, bringing attendance management, employee details, and leave applications together in one place.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
</p>

| Technology | Purpose |
| :--- | :--- |
| Python | Core programming language |
| FastAPI | Backend API development |
| Streamlit | Frontend and dashboard |
| Pydantic | Data validation |
| Requests | HTTP communication between frontend and backend |
| Python-JOSE | JWT-related functionality |
| JSON | Local data persistence |

---

## 📂 Project Structure

We organized our project into separate frontend and backend directories to make the application modular and easier to maintain.

```text
TMS/
├── backend/
│   ├── auth/
│   │   └── auth.py
│   ├── Database/
│   │   ├── attendance.json
│   │   ├── details.json
│   │   ├── leaves.json
│   │   └── register.json
│   ├── repository/
│   │   ├── attendance.py
│   │   ├── breaks_cal.py
│   │   ├── details.py
│   │   ├── leaves.py
│   │   ├── login.py
│   │   └── Register.py
│   ├── routes/
│   │   ├── attendance.py
│   │   ├── details.py
│   │   ├── leaves.py
│   │   ├── login.py
│   │   └── Register.py
│   ├── services/
│   │   ├── attendance.py
│   │   ├── details.py
│   │   ├── leaves.py
│   │   ├── login.py
│   │   ├── Register.py
│   │   ├── Location_based_check_in.py
│   │   └── __init__.py
│   └── main.py
├── frontend/
│   ├── app.py
│   ├── Dashboard.py
│   ├── Dashboard_aqsa.py
│   ├── location.py
│   ├── login.py
│   └── Register.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Backend Architecture

We divided the backend into separate layers, each responsible for a specific part of the application.

<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>routes/</code></td>
      <td>Defines API endpoints and handles incoming requests.</td>
    </tr>
    <tr>
      <td><code>services/</code></td>
      <td>Contains business logic for application operations.</td>
    </tr>
    <tr>
      <td><code>repository/</code></td>
      <td>Handles JSON file reading and writing.</td>
    </tr>
    <tr>
      <td><code>Database/</code></td>
      <td>Stores employee and application records.</td>
    </tr>
    <tr>
      <td><code>auth/</code></td>
      <td>Contains authentication-related functionality.</td>
    </tr>
  </tbody>
</table>

Our main backend entry point is <code>backend/main.py</code>, where we register the API routes.

### API Endpoints

| Endpoint | Purpose |
| :--- | :--- |
| `/login` | Employee authentication |
| `/register/employee` | Employee registration |
| `/details` | Employee details |
| `/leave` | Submit leave application |
| `/leaves` | Retrieve leave records |
| `/checkin` | Record check-in |
| `/checkout` | Record check-out |
| `/break/start` | Start a break |
| `/break/resume` | Resume work |
| `/tabledata` | Retrieve tabular data |

<sub>Note: The HTTP methods, request parameters, and authentication requirements depend on the implementation of each endpoint.</sub>

## 🖥️ Frontend Architecture

We used Streamlit to build the employee-facing interface and Requests to communicate with the FastAPI backend.

Our main frontend entry point is <code>frontend/app.py</code>. We used Streamlit session state to manage page navigation between:

<ul>
  <li>Login page</li>
  <li>Registration page</li>
  <li>Employee dashboard</li>
  <li>Location verification page</li>
</ul>

Through the interface, employees can manage attendance, submit leave applications, and view their personal information.

## 💾 Data Storage

We used JSON files to keep the project lightweight and straightforward to run during development.

| File | Description |
| :--- | :--- |
| `register.json` | Employee registration records |
| `attendance.json` | Attendance and related records |
| `leaves.json` | Leave applications |
| `details.json` | Employee personal information |

This approach allowed us to implement data persistence without setting up an external database server. For a production environment, we would consider migrating to PostgreSQL or another database that supports reliable concurrent access.

---

## 🚀 Getting Started

### Prerequisites

Before running our project, we need:

<ul>
  <li>Python 3.10 or newer</li>
  <li>pip package manager</li>
  <li>A terminal or command prompt</li>
  <li>A web browser</li>
</ul>

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd TMS
```

### 2. Create a Virtual Environment

```bash
python -m venv pvenv
```

### 3. Activate the Environment

For Windows:

```bash
pvenv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Backend

Open a terminal from the project root and run:

```bash
cd backend
uvicorn main:app --reload
```

The backend will normally be available at:

<ul>
  <li><strong>API:</strong> <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></li>
  <li><strong>Swagger Documentation:</strong> <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
</ul>

### 6. Run the Frontend

Open a second terminal from the project root, activate the virtual environment, and run:

```bash
cd frontend
streamlit run app.py
```

Streamlit will launch the application in the browser.

---

## 🔄 Application Workflow

<ol>
  <li>
    <strong>Registration:</strong> Employees enter their personal information to create an account.
  </li>
  <li>
    <strong>Login:</strong> The backend validates credentials and generates a JWT after successful authentication.
  </li>
  <li>
    <strong>Dashboard:</strong> Authenticated employees access the available application features.
  </li>
  <li>
    <strong>Attendance:</strong> Employees use the check-in, check-out, and break management features, with location verification where configured.
  </li>
  <li>
    <strong>Leave Management:</strong> Employees submit leave applications and retrieve their leave records.
  </li>
  <li>
    <strong>Personal Details:</strong> Employees view the information associated with their accounts.
  </li>
</ol>

## 📚 What We Learned

Through this group project, we gained practical experience in full-stack application development and learned how different components work together.

<ul>
  <li>Building REST APIs using FastAPI.</li>
  <li>Creating interactive interfaces using Streamlit.</li>
  <li>Structuring applications using routes, services, and repositories.</li>
  <li>Validating data using Pydantic.</li>
  <li>Working with JWT-based authentication.</li>
  <li>Connecting frontend applications to backend APIs.</li>
  <li>Implementing JSON-based data persistence.</li>
  <li>Developing attendance, break-tracking, and leave management workflows.</li>
  <li>Integrating location verification into an application workflow.</li>
  <li>Collaborating as a team to develop and integrate different modules.</li>
</ul>

## 🔮 Future Improvements

We identified several areas for further development:

<ul>
  <li>Migrate JSON storage to PostgreSQL or another production-ready database.</li>
  <li>Strengthen password security using secure password hashing.</li>
  <li>Protect private API endpoints through JWT verification.</li>
  <li>Implement token expiration, logout, and role-based access control.</li>
  <li>Add leave approval and rejection functionality.</li>
  <li>Improve exception handling, logging, and automated testing.</li>
  <li>Enhance location verification and attendance validation.</li>
  <li>Deploy the application in a secure hosting environment.</li>
</ul>

## Our Team

We developed this project collaboratively, contributing to the design, implementation, and integration of the different modules. Working together helped us understand the practical challenges involved in building a full-stack employee management application.

## Conclusion

As a team, we developed the Talent Management System to bring employee registration, authentication, attendance tracking, leave management, and personal information into one application.

By combining FastAPI, Streamlit, JWT authentication, and JSON-based persistence, we created a practical project that helped us apply our programming and software development knowledge to a real-world use case.

We see this project as an important step in our learning journey and a foundation for further improvements in security, scalability, and functionality.
