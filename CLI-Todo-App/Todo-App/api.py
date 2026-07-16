from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def root():
    return {"message: Todo backend is running"}



