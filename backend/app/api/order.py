from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.kite_session import get_kite_with_token

router = APIRouter()

class OrderRequest(BaseModel):
    symbol: str
    quantity: int
    transaction_type: str  # "BUY" or "SELL"

@router.post("/place-order")
def place_order(order: OrderRequest):
    kite = get_kite_with_token()

    try:
        # Fetch instrument_token from symbol
        instruments = kite.instruments("NSE")
        match = next((i for i in instruments if i["tradingsymbol"] == order.symbol.upper()), None)

        if not match:
            raise HTTPException(status_code=404, detail="Symbol not found")

        response = kite.place_order(
            tradingsymbol=order.symbol.upper(),
            exchange="NSE",
            transaction_type=order.transaction_type.upper(),
            quantity=order.quantity,
            order_type="MARKET",
            product="MIS",
            variety="regular"
        )

        return {"message": "✅ Order placed", "order_id": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
