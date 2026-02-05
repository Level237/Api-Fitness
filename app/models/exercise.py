from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List
from uuid import UUID,uuid4

class Exercise(SQLModel,table=True):
    id:UUID = Field(default=uuid4(),primary_key=True,index=True)
    title:str = Field(index=True)
    description:Optional[str] = None
    
    video_url:str

    muscle_group:str
    equipment_needed : Optional[str] = "Aucun"

    is_premium : bool = Field(default=False)

    workouts: List["WorkoutExercise"] = Relationship(back_populates="exercise")
