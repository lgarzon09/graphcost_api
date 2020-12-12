from pydantic import BaseModel

class ReceptionistsInDB(BaseModel):
  rec_id: int
  rec_hot_id: int # Tener en cuenta
  rec_name: str
  rec_doc: str
  rec_email: str
  rec_phone: str

