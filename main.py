import uvicorn
from fastapi import FastAPI
from src.handlers.predict import model_post_handler
from src.entities.prediction_request import PredictionRequestPydantic
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get('/')
def hello_world():
    return {'Hello': 'World'}

@app.post('/predict/')
def predict(req: PredictionRequestPydantic):
    return JSONResponse(content = model_post_handler(req))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
