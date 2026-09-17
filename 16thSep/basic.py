from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def hey():
    return {'message':'Hello World'}
@app.get('/about')
def about():
    return{'message':'This msg is problematic'}
@app.get('/about/hmm')
def hmm():
    return {'message':'THE LAST PAGE'}
