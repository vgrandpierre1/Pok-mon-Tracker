from fastapi import FastAPI

app = FastAPI(title="Pokemon Cardmarket Tracker")

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running"}

@app.get("/api/collection")
def collection():
    # Données de test (on remplacera par Cardmarket ensuite)
    cards = [
        {"name": "Pikachu", "set": "Base Set", "qty": 2, "unit_price": 8.40},
        {"name": "Charizard", "set": "Base Set", "qty": 1, "unit_price": 250.00},
    ]
    total = sum(c["qty"] * c["unit_price"] for c in cards)
    return {"cards": cards, "total_value": total}
