from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
)


class UserSchema(BaseModel):
    id: int = Field(alias="_id", gt=0)
    profile_id: int = Field(gt=0)

    phone_number: str = Field(max_length=15)
    password: str = Field()
    active: bool = Field(default=True)

    created_at: datetime = Field(default=datetime.now())
    created_by: str = Field()
    updated_at: datetime = Field(default=datetime.now())
    updated_by: str = Field()

    class Config:
        exclude = ['password', ]

        json_schema_extra = {
            'example': {
                'id': 1,
                'profile_id': 1,
                'phone_number': '+7(777)777-77-77',
                'password': 's0me_h@$h_wh1cH_1$_VeRY_L0#6',
                'active': True,
                'created_at': datetime(2024, 1, 1, 0, 0, 0, 0),
                'created_by': 'admin',
                'updated_at': datetime(2024, 1, 1, 0, 0, 0, 0),
                'updated_by': 'admin',
            }
        }
