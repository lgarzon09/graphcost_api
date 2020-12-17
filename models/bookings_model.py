from pydantic import BaseModel

class BookingsIn(BaseModel):
  boo_cli_id: int
  boo_dateIN: str
  boo_dateOUT: str
  boo_roo_id: int # Esto es el tipo
  boo_name_roo: str
  boo_rec_id: int # ID del recepcionista
  boo_price_charged: int

class BookingsOut(BaseModel):
  boo_id: int
  boo_cli_id: int
  boo_dateIN: str
  boo_dateOUT: str
  boo_name_roo: str
  boo_rec_id: int
  boo_price_charged: int