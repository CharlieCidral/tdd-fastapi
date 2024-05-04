from pydantic import UUID4, BaseModel, model_validator, Field
from datetime import datetime
from bson import Decimal128
from decimal import Decimal


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributtes = True


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator(mode="before")
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data
