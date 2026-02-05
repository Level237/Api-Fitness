from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID,uuid4

class WorkoutExercise(SQLModel, table=True):
    __tablename__ = "workout_exercises"
    id:UUID = Field(default=uuid4(),primary_key=True,index=True)
    workout_id: int = Field(foreign_key="workouts.id", primary_key=True)
    exercise_id: int = Field(foreign_key="exercises.id", primary_key=True)

    order:int = Field(default=1)
    reps:Optional[int] = None
    duration:Optional[int] = None
    rest_time:int = Field(default=30)