from pydantic import BaseModel
from typing import Dict

class RoomsInDB(BaseModel):
  roo_id: int = 0
  roo_price: int
  roo_maintenance_cost: int
  roo_type: str
  roo_description: str
  roo_total: int

#USAR CON DICT
database_rooms = Dict[str, RoomsInDB]

database_rooms = {
  "A": RoomsInDB(**{
    "roo_id": 1,
    "roo_price": 80000,
    "roo_maintenance_cost": 70000,
    "roo_type": "A",
    "roo_description": "Habitación de tipo 1",
    "roo_total": 10
  }),
}

def get_room(roo_type: str):
  if roo_type in database_rooms.keys():
    return database_rooms[roo_type]
  else:
    return None

def get_all_rooms():
  return database_rooms

generator = {"id": 1}

def save_room(room_in_db: RoomsInDB):
  generator["id"] = generator["id"] + 1
  room_in_db.roo_id = generator["id"]

  database_rooms[room_in_db.roo_type] = room_in_db

  return room_in_db