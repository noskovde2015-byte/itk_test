from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator


class UserBase(BaseModel):
    """Base User shema"""
    name: str = Field(min_length=2, max_length=20, description="User firs name")
    surname: str = Field(min_length=2, max_length=20, description="User surname")
    age: int = Field(ge=0, le=150, description="User age")
    email: EmailStr

    @field_validator("age", mode="before")
    def age_validator(cls, v):
        if v < 0:
            raise ValueError("age can not be negative")
        return v


class UserCreate(UserBase):
    """Shema for creating a new user"""
    pass


class UserUpdate(UserCreate):
    """Schema for updating user"""
    pass


class UserRead(UserBase):
    """Shema for reading a user"""
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
