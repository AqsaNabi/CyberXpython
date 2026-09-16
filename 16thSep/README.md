<h2>Application programming interface API</h2>
APIs are mechanisms that enable two software components such as frontend and backend of an application to commuinicate with each other using a defined set of rules, protocols and data format
<h3>NEED FOR APIs</h3>
provides Security via acting as an interface between frontend and backend and not allowing direct interaction with the backend or database. With the help of the API, one backend can maintain different type of frontends.
<h2>FastAPI </h2>
is a modern, high-performance web framework for building APIs with python. It is made upon two libraries Starlette and Pydantic, Starlette handles , or manages how our request and response are send. Pydantic is a data validation library, is used to check if the data coming into you API is correct and in the right format.
Prior to fastapi the frameworks did existed but there was performace issue as they have slow response time. Also complex and unnecessary code, fast to code.
<h2> Installation of fastApi in VScode</h2>
first i created a virtual named fastvenv and i  then installed uvicorn library using pip install fastapi uvicorn command in terminal
After installation i created a file within the venv naming main.py and i imported fastApi. Then created an object of the fastAPI class naming it as app. To fetch data from the server we use get and if we want to send data to the server we use post. For end-point a route is defined using @app.get("/url")
