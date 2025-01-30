from datetime import datetime
from sqlalchemy import Column, UUID, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base
from pydantic import BaseModel

class Feedback(Base):
    __tablename__ = 'feedback'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey('documents.id'))
    rating = Column(Float)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    metadata = Column(JSONB)

class FeedbackCreate(BaseModel):
    document_id: UUID
    rating: float
    comment: str

class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    current_version = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DocumentVersion(Base):
    __tablename__ = 'document_versions'
    
    document_id = Column(UUID(as_uuid=True), ForeignKey('documents.id'), primary_key=True)
    version = Column(Integer, primary_key=True)
    title = Column(String)
    content_type = Column(String)
    storage_path = Column(String)
    metadata = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
