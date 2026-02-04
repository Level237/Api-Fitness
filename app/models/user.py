from sqmodel import SQLModel,Field,JSON,Column
from typing import Optional,List
from datetime import datetime
from uuid import UUID,uuid4
from enum import Enum

class Gender(str,Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class ActivityLevel(str,Enum):
    SEDENTARY = "sedentary"
    LIGHTLY_ACTIVE = "legerement_actif"
    MODERATELY_ACTIVE = "moderement_actif"
    VERY_ACTIVE = "tres_actif

class UserBase(SQLModel):
    email : str = Field(index=True,unique=True,nullable=False)
    phone : str = Field(index=True,unique=True,nullable=True)
    user_name : Optional[str] = Field(index=True,unique=True,nullable=False)

    gender:Optional[Gender] = None
    weight:Optional[float] = None
    activity_level:Optional[ActivityLevel] = None

    motivations: List[str] = Field(default=[], sa_column=Column(JSON))
    is_active : bool = Field(default=True)
    is_premium : bool = Field(default=False)

    main_goal : Optional[str] = None

    fitness_level : Optional[str] = None
    
class User(UserBase,table=True):

    id:UUID = Field(default=uuid4(),primary_key=True,index=True)
    hashed_password : str = Field(nullable=False)
    created_at : datetime = Field(default=datetime.now())
    updated_at : datetime = Field(default=datetime.now())
    
    