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
    "roo_price": 90000,
    "roo_maintenance_cost": 70000,
    "roo_type": "A",
    "roo_description": "Individual",
    "roo_total": 15
  }),
  "B": RoomsInDB(**{
    "roo_id": 2,
    "roo_price": 120000,
    "roo_maintenance_cost": 120000,
    "roo_type": "B",
    "roo_description": "Doble",
    "roo_total": 10
  }),
  "C": RoomsInDB(**{
    "roo_id": 3,
    "roo_price": 100000,
    "roo_maintenance_cost": 150000,
    "roo_type": "C",
    "roo_description": "Triple",
    "roo_total": 5
  }),
  "D": RoomsInDB(**{
    "roo_id": 4,
    "roo_price": 200000,
    "roo_maintenance_cost": 250000,
    "roo_type": "D",
    "roo_description": "Quad",
    "roo_total": 5
  }),
  "E": RoomsInDB(**{
    "roo_id": 5,
    "roo_price": 300000,
    "roo_maintenance_cost": 350000,
    "roo_type": "E",
    "roo_description": "Queen",
    "roo_total": 5
  })
}

def get_room(roo_type: str):
  if roo_type in database_rooms.keys():
    return database_rooms[roo_type]
  else:
    return None

def get_all_rooms():
  return database_rooms

def get_total_rooms():
  total_rooms = 0
  
  for roo_type in database_rooms.keys():
    total_rooms += database_rooms[roo_type].roo_total

  return total_rooms

generator = {"id": 5}

def save_room(room_in_db: RoomsInDB):
  generator["id"] = generator["id"] + 1
  room_in_db.roo_id = generator["id"]

  database_rooms[room_in_db.roo_type] = room_in_db

  return room_in_db