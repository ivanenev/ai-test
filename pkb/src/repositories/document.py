from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from ..models.document import Document, DocumentVersion

class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_document(self, title: str, content_type: str, 
                       storage_path: str, metadata: dict) -> UUID:
        document_id = uuid4()
        document = Document(
            id=document_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        version = DocumentVersion(
            document_id=document_id,
            version=1,
            title=title,
            content_type=content_type,
            storage_path=storage_path,
            metadata=metadata,
            created_at=datetime.utcnow()
        )
        
        self.db.add(document)
        self.db.add(version)
        self.db.commit()
        
        return document_id

    def get_document(self, document_id: UUID, version: Optional[int] = None):
        if version:
            return self.db.query(DocumentVersion).filter(
                DocumentVersion.document_id == document_id,
                DocumentVersion.version == version
            ).first()
        else:
            document = self.db.query(Document).get(document_id)
            if document:
                return self.db.query(DocumentVersion).filter(
                    DocumentVersion.document_id == document_id,
                    DocumentVersion.version == document.current_version
                ).first()
            return None
