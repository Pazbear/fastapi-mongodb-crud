from typing import Optional
from pydantic import BaseModel, BaseConfig, EmailStr, Field

class User(BaseModel):
    id: Optional[str] = None
    nickname : str
    email : EmailStr
    password : str
    class Config(BaseConfig):
        allow_population_by_field_name=True