import asyncio
from surrealdb import Surreal

from surreal_health.utils.surreal import (
    DeviceHandler, 
    PersonHandler, 
    SupplementHandler, 
    InterventionHandler, 
    MeasurementHandler
)

async def main():
    async with Surreal("ws://localhost:8977/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")

        # Device example
        device_handler = DeviceHandler(db)
        new_device_id = await device_handler.create({"name": "Blood Pressure Monitor", "type": "Wearable"})
        if new_device_id:
            read_device = await device_handler.read(new_device_id)
            updated_device = await device_handler.update(new_device_id, {"type": "Medical"})
            all_devices = await device_handler.search("type = 'Medical'")
            await device_handler.delete(new_device_id)
            print(read_device, updated_device, all_devices)

        # Person example
        person_handler = PersonHandler(db)
        new_person_id = await person_handler.create({"name": "Alice", "age": 30})
        if new_person_id:
            read_person = await person_handler.read(new_person_id)
            updated_person = await person_handler.update(new_person_id, {"age": 31})
            all_persons = await person_handler.search("age > 20")
            await person_handler.delete(new_person_id)
            print(read_person, updated_person, all_persons)

        # Supplement example
        supplement_handler = SupplementHandler(db)
        new_supplement_id = await supplement_handler.create({"name": "Vitamin D", "type": "Nutritional"})
        if new_supplement_id:
            read_supplement = await supplement_handler.read(new_supplement_id)
            updated_supplement = await supplement_handler.update(new_supplement_id, {"type": "Dietary"})
            all_supplements = await supplement_handler.search("type = 'Dietary'")
            await supplement_handler.delete(new_supplement_id)
            print(read_supplement, updated_supplement, all_supplements)

        # Intervention example
        intervention_handler = InterventionHandler(db)
        new_intervention_id = await intervention_handler.create({"name": "Cardio Training", "type": "Exercise"})
        if new_intervention_id:
            read_intervention = await intervention_handler.read(new_intervention_id)
            updated_intervention = await intervention_handler.update(new_intervention_id, {"type": "High-Intensity Exercise"})
            all_interventions = await intervention_handler.search("type = 'High-Intensity Exercise'")
            await intervention_handler.delete(new_intervention_id)
            print(read_intervention, updated_intervention, all_interventions)

        # Measurement example
        measurement_handler = MeasurementHandler(db)
        new_measurement_id = await measurement_handler.create({"type": "heart_rate", "value": 72, "timestamp": "2024-05-04T12:00:00Z"})
        if new_measurement_id:
            read_measurement = await measurement_handler.read(new_measurement_id)
            updated_measurement = await measurement_handler.update(new_measurement_id, {"value": 75})
            all_measurements = await measurement_handler.search("type = 'heart_rate'")
            await measurement_handler.delete(new_measurement_id)
            print(read_measurement, updated_measurement, all_measurements)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())