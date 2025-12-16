from fastapi import FastAPI

app = FastAPI(title="Pokemon Cardmarket Tracker")

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running"}

@app.get("/api/collection")
def collection():
    return {
        "cards": [],
        "total_value": 0
    }
