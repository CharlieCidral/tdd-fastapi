from datetime import datetime
import uuid
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: datetime = Field(default_factory=lambda: datetime.now().isoformat())
