from fastapi import APIRouter, HTTPException
from uuid import UUID
from typing import List
from ..models.document import DocumentVersion
from ..repositories.document import DocumentRepository
from ..dependencies import get_db

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.get("/", response_model=List[DocumentVersion])
async def list_documents(db: Session = Depends(get_db)):
    repo = DocumentRepository(db)
    # Get latest version of each document
    documents = []
    for doc in repo.filter():
        latest = repo.get_document(doc.id)
        if latest:
            documents.append(latest)
    return documents

@router.get("/{document_id}", response_model=DocumentVersion)
async def get_document(document_id: UUID, db: Session = Depends(get_db)):
    repo = DocumentRepository(db)
    document = repo.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
