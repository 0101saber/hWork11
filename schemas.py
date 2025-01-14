from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class OwnerSchema(BaseModel):
    fullname: str
    email: EmailStr


class OwnerResponse(OwnerSchema):
    id: int = 1

    class Config:
        from_attributes = True


class CatBase(BaseModel):
    nick: str = Field('Simon', min_length=3, max_length=25)
    age: int = Field(1, ge=1, le=25)
    vaccinated: Optional[bool] = None


class CatSchema(CatBase):
    owner_id: int = Field(1, ge=1)


class CatResponse(CatSchema):
    id: int = 1
    owner: OwnerResponse = Field()

    class Config:
        from_attributes = True
