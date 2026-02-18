from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.sos import router as sos_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="CrowdSenseNeo API",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register routes
app.include_router(chat_router)
app.include_router(sos_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}