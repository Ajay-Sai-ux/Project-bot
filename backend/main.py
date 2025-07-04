from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, order
from app.core.kite_ws import start_kite_ws

app = FastAPI(
    title="Kite Connect API",
    description="API for Kite Connect integration",
    version="1.0.0"
)

# ✅ CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    start_kite_ws()


@app.get("/")
def read_root():
    return {"message": "✅ fastapi-kite-connect is running!"}

# ✅ Include routers AFTER setting up middleware
app.include_router(auth.router, prefix="/auth")
app.include_router(order.router, prefix="/trade")