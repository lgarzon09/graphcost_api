from pydantic import BaseModel
from datetime import date

class BookingsIn(BaseModel):
  boo_cli_id: int
  boo_dateIN: str
  boo_dateOUT: str
  boo_roo_id: int # Esto es el tipo
  boo_name_roo: str
  boo_rec_id: int # ID del recepcionista

class BookingsOut(BaseModel):
  boo_id: int
  boo_cli_id: int
  boo_dateIN: str
  boo_dateOUT: str
  boo_roo_id: int
  boo_name_roo: str
  boo_rec_id: int
  boo_price_charged: int