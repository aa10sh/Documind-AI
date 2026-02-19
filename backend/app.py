from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



from backend.config.settings import APP_NAME, APP_VERSION
from backend.config.logging import logger

# Import API routers (we will create them next)
from backend.api.upload_routes import router as upload_router
from backend.api.chat_routes import router as chat_router
from backend.api.health_routes import router as health_router

# Create FastAPI App
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

# Enable CORS (Frontend ↔ Backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production we restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMind AI 🚀",
        "version": APP_VERSION
    }

# Include API Routes
app.include_router(upload_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
app.include_router(health_router, prefix="/api")

logger.info("FastAPI app initialized successfully 🚀")