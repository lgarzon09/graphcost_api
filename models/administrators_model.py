from pydantic import BaseModel

class AdministratorsIn(BaseModel):
  adm_hot_id: int # Tener en cuenta
  adm_name: str
  adm_doc: str
  adm_email: str
  adm_phone: str

class AdministratorsIn(BaseModel):
  adm_hot_id: int # Tener en cuenta
  adm_name: str
  adm_doc: str
  adm_email: str
  adm_phone: str