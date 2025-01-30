from typing import Optional, Dict, Any
from uuid import UUID
from ..models.document import DocumentVersion, Feedback
from ..repositories.document import DocumentRepository
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class BrowserController:
    """Agent that handles browser interactions and feedback analysis"""
    
    def __init__(self, db: Session):
        self.db = db
        self.document_repo = DocumentRepository(db)
        
    def analyze_feedback(self, document_id: UUID) -> Dict[str, Any]:
        """Analyze feedback for a specific document"""
        feedbacks = self.document_repo.filter(Feedback.document_id == document_id)
        
        if not feedbacks:
            return {"message": "No feedback available for this document"}
            
        total_ratings = sum(f.rating for f in feedbacks)
        average_rating = total_ratings / len(feedbacks)
        
        # Basic sentiment analysis
        positive_count = sum(1 for f in feedbacks if f.rating >= 4)
        negative_count = sum(1 for f in feedbacks if f.rating <= 2)
        
        return {
            "document_id": str(document_id),
            "total_feedbacks": len(feedbacks),
            "average_rating": round(average_rating, 1),
            "positive_feedbacks": positive_count,
            "negative_feedbacks": negative_count,
            "recent_comments": [f.comment for f in feedbacks[-3:] if f.comment]
        }
        
    def get_document_metadata(self, document_id: UUID) -> Optional[Dict[str, Any]]:
        """Get metadata and usage statistics for a document"""
        document = self.document_repo.get_document(document_id)
        if not document:
            return None
            
        feedback_stats = self.analyze_feedback(document_id)
        
        return {
            "document_id": str(document_id),
            "title": document.title,
            "version": document.version,
            "created_at": document.created_at.isoformat(),
            "feedback_stats": feedback_stats,
            "total_views": document.metadata.get("views", 0),
            "last_accessed": document.metadata.get("last_accessed")
        }
