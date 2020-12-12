from pydantic import BaseModel

class HotelIn(BaseModel):
  hot_name: str
  hot_nit: str
  hot_email: str
  hot_cel: str
  hot_phone: str
  hot_city: str
  hot_address: str

class HotelOut(BaseModel):
  hot_name: str
  hot_nit: str
  hot_email: str
  hot_cel: str
  hot_phone: str
  hot_city: str
  hot_address: str