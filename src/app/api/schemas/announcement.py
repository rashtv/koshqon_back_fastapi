from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
)


class AnnouncementSchema(BaseModel):
    id: int = Field(alias='_id', gt=0)
    user_id: int = Field(gt=0)

    city: str = Field(max_length=255)
    district: str = Field(max_length=255)
    street: str = Field(max_length=255)
    house_number: str = Field(max_length=255)

    type: str = Field()
    room_number: int = Field(gt=1, le=99)
    floors_number: int = Field(gt=0, le=99)
    floor_location: int = Field(gt=0, le=99)
    area: int = Field(gt=0)
    living_area: int = Field(gt=0)
    bathroom_area: int = Field(ge=0)
    kitchen_area: int = Field(ge=0)

    condition: str = Field(max_length=255)
    description: str = Field(max_length=1023)

    created_at: datetime = Field()
    updated_at: datetime = Field()

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                'user_id': 1,
                'city': 'Almaty',
                'district': 'Bostandyk',
                'street': 'Samal-1',
                'house_number': '1/1',
                'type': 'apartment',
                'room_number': 1,
                'floors_number': 10,
                'floor_location': 1,
                'area': 50,
                'bathroom_area': 10,
                'kitchen_area': 10,
                'conditions': 'well-done',
                'description': 'searching for roommates...',
                'created_at': datetime(2024, 1, 1, 0, 0, 0, 0),
                'updated_at': datetime(2024, 1, 1, 0, 0, 0, 0),
            }
        }
