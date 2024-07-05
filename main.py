# 1. Library imports
import uvicorn
from fastapi import FastAPI


# 2. create app object
app = FastAPI()

# 3. index route create
@app.get('/')
def index():
    return {'message': 'API working connection'}

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=1000)

