from pydantic import BaseModel
from typing import Dict

class HotelInDB(BaseModel):
  hot_id: int = 0
  hot_name: str
  hot_nit: str
  hot_email: str
  hot_cel: str
  hot_phone: str
  hot_city: str
  hot_address: str

database_hotel = Dict[str, HotelInDB]

database_hotel = {
  "DescansaBien": HotelInDB(**{
  "hot_id": 1,
	"hot_name": "DescansaBien",
	"hot_nit": "11.338.854-3",
	"hot_email": "descansabien@hotel.com",
	"hot_cel": "3124567890",
	"hot_phone": "5612345",
	"hot_city": "Bogotá",
	"hot_address": "Calle 2 No. 34 - 12"
  }),
}

generator = {"id": 1}

def save_hotel(hotel_in_db: HotelInDB):
  generator["id"] = generator["id"] + 1
  hotel_in_db.hot_id = generator["id"]

  database_hotel[hotel_in_db.hot_name] = hotel_in_db

  return hotel_in_db

# Por ahora es estático !!!!!!!!!!!!!!!!!!!!!!!
def get_info_hotel():
	return database_hotel["DescansaBien"]
