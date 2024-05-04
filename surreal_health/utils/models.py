# surreal_health/utils/models.py

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Device(BaseModel):
    name: str
    type: str
    manufacturer: str
    identifier: str
    serial_number: str


class Person(BaseModel):
    name: str
    age: int
    gender: str
    health_conditions: Optional[List[str]] = Field(default_factory=list)


class Supplement(BaseModel):
    name: str
    type: str
    description: str
    target_person: Optional[Person] = None


class Intervention(BaseModel):
    name: str
    type: str
    description: str
    target_device: Optional[Device] = None
    target_person: Optional[Person] = None
    supplement: Optional[Supplement] = None


class Measurement(BaseModel):
    type: str
    value: float
    timestamp: datetime
    device: Optional[Device] = None
    person: Optional[Person] = None
