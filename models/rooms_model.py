from pydantic import BaseModel

class RoomsIn(BaseModel):
  roo_price: int
  roo_maintenance_cost: int
  roo_type: str
  roo_description: str
  roo_total: int

class RoomsOut(BaseModel):
  roo_id: int
  roo_price: int
  roo_maintenance_cost: int
  roo_type: str
  roo_description: str
  roo_total: int