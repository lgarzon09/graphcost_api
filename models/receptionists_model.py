from pydantic import BaseModel

class ReceptionistsIn(BaseModel):
  rec_hot_id: int
  rec_name: str
  rec_lastname: str
  rec_doc: str
  rec_email: str
  rec_phone: str
  rec_password: str

 class ReceptionistsOut(BaseModel):
  rec_hot_id: int
  rec_name: str
  rec_lastname: str
  rec_doc: str
  rec_email: str
  rec_phone: str