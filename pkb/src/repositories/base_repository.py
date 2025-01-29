from typing import TypeVar, Generic, Optional, List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta

T = TypeVar('T', bound=DeclarativeMeta)

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: T):
        self.db = db
        self.model = model

    def create(self, **kwargs) -> Any:
        entity = self.model(**kwargs)
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get(self, id: Any) -> Optional[T]:
        return self.db.query(self.model).get(id)

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, id: Any, **kwargs) -> Optional[T]:
        entity = self.get(id)
        if entity:
            for key, value in kwargs.items():
                setattr(entity, key, value)
            self.db.commit()
            self.db.refresh(entity)
        return entity

    def delete(self, id: Any) -> bool:
        entity = self.get(id)
        if entity:
            self.db.delete(entity)
            self.db.commit()
            return True
        return False

    def filter(self, **filters) -> List[T]:
        return self.db.query(self.model).filter_by(**filters).all()

    def count(self) -> int:
        return self.db.query(self.model).count()
