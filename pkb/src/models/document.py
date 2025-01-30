from datetime import datetime
from sqlalchemy import Column, UUID, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base

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
