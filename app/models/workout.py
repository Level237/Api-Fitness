
from sqlmodel import SQLModel, Field, Column, JSON, Relationship
from typing import Optional, List
from uuid import UUID,uuid4

class Workout(SQLModel,table=True):
    id:UUID = Field(default=uuid4(),primary_key=True,index=True)
    title:str = Field(index=True)
    difficulty: str
    total_duration: int
    is_premium: bool = Field(default=True)
    thumbnail_url: Optional[str] = None

    exercises: List["WorkoutExercise"] = Relationship(back_populates="workout")

    logs: List["WorkoutLog"] = Relationship()
    
    