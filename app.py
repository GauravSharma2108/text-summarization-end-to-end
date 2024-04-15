from fastapi import FastAPI
import uvicorn
import os
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarization.pipeline.prediction_pipeline import PredictionPipeline
from pydantic import BaseModel

app = FastAPI(
    title="Text Summarization API",
    description="API to summarize text using Pegasus model",
    version="0.0.1"
)

class TextData(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
    
@app.post("/predict")
async def predict_route(data: TextData):
    try:
        obj = PredictionPipeline()
        text = data.text
        text = obj.predict(text)
        return SummarizationResponse(summary=text)
    except Exception as e:
        raise e

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)