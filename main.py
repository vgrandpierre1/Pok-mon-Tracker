from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pokemon Cardmarket Tracker")

# CORS: autorise Webflow + Wized (et autres) à appeler ton API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # on verrouillera plus tard
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running"}

@app.get("/api/collection")
def collection():
    cards = [
        {"name": "Pikachu", "set": "Base Set", "qty": 2, "unit_price": 8.40},
        {"name": "Charizard", "set": "Base Set", "qty": 1, "unit_price": 250.00},
    ]
    total = sum(c["qty"] * c["unit_price"] for c in cards)
    return {"cards": cards, "total_value": total}
