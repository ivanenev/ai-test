from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID
from typing import List
from ..models.document import DocumentVersion, Feedback, FeedbackCreate
from ..repositories.document import DocumentRepository
from ..agents.browser_controller import BrowserController
from ..dependencies import get_db
from sqlalchemy.orm import Session

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

@router.get("/{document_id}/stats")
async def get_document_stats(
    document_id: UUID,
    db: Session = Depends(get_db)
):
    """Get document statistics and feedback analysis"""
    controller = BrowserController(db)
    stats = controller.get_document_metadata(document_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Document not found")
    return stats

@router.post("/{document_id}/feedback")
async def submit_feedback(
    document_id: UUID,
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    repo = DocumentRepository(db)
    document = repo.get(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    feedback_data = Feedback(
        document_id=document_id,
        rating=feedback.rating,
        comment=feedback.comment,
        metadata={}
    )
    db.add(feedback_data)
    db.commit()
    db.refresh(feedback_data)
    
    return {"message": "Feedback submitted successfully", "id": str(feedback_data.id)}
