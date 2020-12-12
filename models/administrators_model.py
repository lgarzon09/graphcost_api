from pydantic import BaseModel

class AdministratorsIn(BaseModel):
  adm_hot_id: int
  adm_name: str
  adm_doc: str
  adm_phone: str

class AdministratorsOut(BaseModel):
  adm_hot_id: int
  adm_name: str
  adm_doc: str
  adm_phone: str