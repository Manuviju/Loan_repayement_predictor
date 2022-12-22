from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form
from pydantic import BaseModel
import pickle
import json

APP_HOST = "0.0.0.0"
APP_PORT = 8000

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")
# Creating base model for input parameters
class input_model(BaseModel):
    Principal:int 
    Terms:int 
    Age:int 
    Gender:int 
    Weekend:int 
    Bechalor:int
    High_School_or_Below:int 
    College:int 

# Loading model
loan_model = pickle.load(open('loan_repayment.sav', 'rb'))

@app.post("/loan_repayment_classifier")
async def loan_status_predict(Principal:int = Form(),
                                Term:int = Form(),
                                Age:int = Form(),
                                Gender:int = Form(),
                                Weekend:int = Form(),
                                Bechalor = Form(),
                                Highschoolorbelow = Form(),
                                College = Form()):

    # input_data = input_parameters.json()
    # input_dict = json.loads(input_data)

    # Principal = input_dict['Principal']
    # Term = input_dict['Terms']
    # Age = input_dict['Age']
    # Gender = input_dict['Gender']
    # Weekend = input_dict['Weekend']
    # Bechalor = input_dict['Bechalor']
    # Highschoolorbelow = input_dict['High_School_or_Below']
    # College = input_dict['College']
    
    input_list = [Principal, Term, Age, Gender, Weekend, Bechalor, Highschoolorbelow, College]

    prediction = loan_model.predict([input_list])


    if prediction == 0:
       return "The repayment can go for collections"

    if prediction[0]== 1:
        return "The person will repay the loan"
    



if __name__=="__main__":
    
    app_run(app, host=APP_HOST, port=APP_PORT)