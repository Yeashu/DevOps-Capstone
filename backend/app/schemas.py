from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class CalculationInput(BaseModel):
    expression: str = Field(min_length=1, max_length=256)
    angle_mode: Literal["rad", "deg"] = "rad"
    label: str = Field(default="", max_length=80)


class LabelUpdate(BaseModel):
    label: str = Field(max_length=80)


class CalculationOutput(CalculationInput):
    model_config = ConfigDict(from_attributes=True)
    id: int
    result: float
    created_at: datetime
