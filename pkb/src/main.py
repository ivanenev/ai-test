from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.document import router as document_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(document_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Personal Knowledge Base API"}
