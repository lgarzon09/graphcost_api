from pydantic import BaseModel

class AdministratorsInDB(BaseModel):
  adm_id: int
  adm_hot_id: int # Tener en cuenta
  adm_name: str
  adm_lastname: str
  adm_doc: str
  adm_email: str
  adm_phone: str
  adm_password: str