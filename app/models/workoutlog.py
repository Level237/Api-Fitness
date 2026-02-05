from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from uuid import UUID,uuid4

class WorkoutLog(SQLModel, table=True):
    __tablename__ = "workout_logs"

    id:UUID = Field(default=uuid4(),primary_key=True,index=True)

    user_id :UUID = Field(foreign_key="users.id", index=True)
    workout_id :UUID = Field(foreign_key="workouts.id", index=True)

    completed_at : datetime = Field(default_factory=datetime.utcnow)
    actual_duration : int
    calories_burned : Optional[int] = None

    # Score de 1 à 5 (1: Trop facile, 5: Épuisant)
    difficulty_feedback : int = Field(default=3)
    user_notes: Optional[str] = None # "Je me sentais fatigué aujourd'hui"

    user: "User" = Relationship(back_populates="workout_logs")
    workout: "Workout" = Relationship(back_populates="workout_logs")
    
    