from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
)


class UserProfileSchema(BaseModel):
    id: int = Field(alias='_id')
    first_name: str = Field()
    last_name: str = Field()
    country: str = Field()
    age: int = Field()
    biography: str = Field()
    text: str = Field()
    rating: float = Field(default=0.0)
    created_at: datetime = Field()
    created_by: str = Field()
    updated_at: datetime = Field()
    updated_by: str = Field()
