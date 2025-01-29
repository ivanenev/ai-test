from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.document import Document, DocumentVersion

class DocumentRepository(BaseRepository[Document]):
    def __init__(self, db: Session):
        super().__init__(db, Document)
        self.version_repo = BaseRepository(db, DocumentVersion)

    def create_document(self, title: str, content_type: str, 
                       storage_path: str, metadata: dict) -> UUID:
        document_id = uuid4()
        document = self.create(
            id=document_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        self.version_repo.create(
            document_id=document_id,
            version=1,
            title=title,
            content_type=content_type,
            storage_path=storage_path,
            metadata=metadata,
            created_at=datetime.utcnow()
        )
        
        return document_id

    def get_document(self, document_id: UUID, version: Optional[int] = None) -> Optional[DocumentVersion]:
        if version:
            return self.version_repo.filter(
                document_id=document_id,
                version=version
            ).first()
        else:
            document = self.get(document_id)
            if document:
                return self.version_repo.filter(
                    document_id=document_id,
                    version=document.current_version
                ).first()
            return None

    def get_document_versions(self, document_id: UUID) -> List[DocumentVersion]:
        return self.version_repo.filter(document_id=document_id)

    def create_version(self, document_id: UUID, title: str, content_type: str,
                      storage_path: str, metadata: dict) -> int:
        document = self.get(document_id)
        if document:
            new_version = document.current_version + 1
            self.version_repo.create(
                document_id=document_id,
                version=new_version,
                title=title,
                content_type=content_type,
                storage_path=storage_path,
                metadata=metadata,
                created_at=datetime.utcnow()
            )
            self.update(document_id, current_version=new_version)
            return new_version
        return 0
