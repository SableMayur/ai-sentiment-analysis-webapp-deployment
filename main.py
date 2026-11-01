from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transformers import pipeline

app = FastAPI()

# Load the sentiment analysis pipeline once on startup
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Sentiment Analysis DevOps Demo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }
                .container { max-width: 500px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
                input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
                input[type="submit"] { background-color: #28a745; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
                input[type="submit"]:hover { background-color: #218838; }
                .result { margin-top: 20px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>AI Sentiment Analysis Tool</h2>
                <form action="/predict" method="post">
                    <label for="text">Enter your text:</label><br>
                    <input type="text" id="text" name="text" placeholder="e.g., Going to gym everyday is good habit!"><br>
                    <input type="submit" value="Analyze Sentiment">
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/predict", response_class=HTMLResponse)
async def predict_sentiment(text: str = Form(...)):
    # Run the Hugging Face pipeline
    result = classifier(text)[0]
    label = result['label']
    score = round(result['score'], 4)
    
    return f"""
    <html>
        <head>
            <title>Result</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }}
                .container {{ max-width: 500px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }}
                a {{ display: inline-block; margin-top: 15px; text-decoration: none; color: #007bff; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Analysis Results</h2>
                <p><strong>Input:</strong> {text}</p>
                <p><strong>Sentiment:</strong> <span style="color: {'green' if label == 'POSITIVE' else 'red'};">{label}</span></p>
                <p><strong>Confidence Score:</strong> {score}</p>
                <a href="/">← Back to Analyzer</a>
            </div>
        </body>
    </html>
    """