# 1. Library imports
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


# 2. create app object
app = FastAPI()

# 3. index route create
@app.get('/')
def index():
    return {'message': 'API working connection'}

# write a route to save and map short url to long one in the Database

@app.get('/shorturl')
def redirector():
    # this function can be taking the shorturl as the parameter and finding the corrosponding long url to this short url and than redirect to the long url
    # here the status code is important without providing the correct status code redirection wont happen
    return RedirectResponse(
        url="https://api.slingacademy.com", status_code=302
    )

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=1000)

