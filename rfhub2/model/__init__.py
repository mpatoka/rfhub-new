from pydantic import BaseModel
from typing import List, Optional


class NestedCollection(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class KeywordUpdate(BaseModel):
    name: str
    doc: Optional[str]
    args: Optional[str]

    class Config:
        orm_mode = True


class KeywordCreate(KeywordUpdate):
    collection_id: int


class CollectionUpdate(BaseModel):
    name: str
    type: Optional[str]
    version: Optional[str]
    scope: Optional[str]
    named_args: Optional[str]
    path: Optional[str]
    doc: Optional[str]
    doc_format: Optional[str]


class NestedKeyword(KeywordUpdate):
    id: int


class Collection(NestedCollection, CollectionUpdate):
    keywords: List[NestedKeyword]


class Keyword(NestedKeyword):
    collection: NestedCollection
