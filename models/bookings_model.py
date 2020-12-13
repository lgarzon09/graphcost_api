from pydantic import BaseModel
from datetime import date

class BookingsIn(BaseModel):
  boo_cli_id: int
  boo_dateIN: date
  boo_dateOUT: date
  boo_roo_id: int # Esto es el tipo
  boo_name_roo: str
  boo_rec_id: int # ID del recepcionista
  boo_price_charged: int

class BookingsOut(BaseModel):
  boo_cli_id: int
  boo_dateIN: date
  boo_dateOUT: date
  boo_name_roo: str
  boo_price_charged: int