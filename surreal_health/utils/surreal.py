# app_dir/utils/surreal.py

from typing import List, Optional, Union
from datetime import datetime
from surrealdb import Surreal
from surreal_health.utils.models import (
    Device, 
    Person, 
    Supplement, 
    Intervention, 
    Measurement
)


class SurrealDBHandler:
    def __init__(self, db: Surreal, table_name: str):
        self.db = db
        self.table_name = table_name

    async def create(self, record_data: dict):
        result = await self.db.create(self.table_name, record_data)
        if result is None or not isinstance(result, dict) or 'id' not in result:
            return None
        return result['id']

    async def read(self, record_id: Union[int, str]):
        result = await self.db.select(f"{self.table_name}:{record_id}")
        return result

    async def update(self, record_id: Union[int, str], updates: dict):
        result = await self.db.update(f"{self.table_name}:{record_id}", updates)
        return result

    async def delete(self, record_id: Union[int, str]):
        result = await self.db.delete(f"{self.table_name}:{record_id}")
        return result

    async def search(self, query: str):
        result = await self.db.query(f"SELECT * FROM {self.table_name} WHERE {query}")
        return result

class DeviceHandler(SurrealDBHandler):
    def __init__(self, db: Surreal):
        super().__init__(db, "devices")


class PersonHandler(SurrealDBHandler):
    def __init__(self, db: Surreal):
        super().__init__(db, "persons")


class SupplementHandler(SurrealDBHandler):
    def __init__(self, db: Surreal):
        super().__init__(db, "supplements")


class InterventionHandler(SurrealDBHandler):
    def __init__(self, db: Surreal):
        super().__init__(db, "interventions")


class MeasurementHandler(SurrealDBHandler):
    def __init__(self, db: Surreal):
        super().__init__(db, "measurements")