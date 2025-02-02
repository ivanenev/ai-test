from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.document import router as document_router

app = FastAPI()

# Include document routes
app.include_router(document_router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Personal Knowledge Base API"}

# For development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
