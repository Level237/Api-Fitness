
from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, List
from uuid import UUID,uuid4

class Workout(SQLModel,table=True):
    id:UUID = Field(default=uuid4(),primary_key=True,index=True)
    title:str = Field(index=True)
    difficulty: str
    total_duration: int
    structure: List[dict] = Field(default=[], sa_column=Column(JSON))
    is_premium: bool = Field(default=True)
    thumbnail_url: Optional[str] = None
    
    