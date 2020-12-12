from pydantic import BaseModel

class AdministratorsInDB(BaseModel):
  adm_id: int = 0
  adm_hot_id: int # Tener en cuenta
  adm_name: str
  adm_doc: str
  adm_phone: str

database_administrators = Dict[str, AdministratorsInDB]

database_administrators = {
  "ann@hotel.com": AdministratorssInDB(**{
    "adm_id": 1,
    "adm_hot_id": 1, # Tener en cuenta
    "adm_name": "Ann A",
    "adm_doc": "1029384756",
    "adm_phone": "3120496751"
  })
}

generator = {"id": 1}

def save_administrator(administrator_in_db: AdministratorsInDB):
  generator["id"] = generator["id"] + 1
  administrator_in_db.cli_id = generator["id"]

  database_administrators[administrator_in_db.cli_email] = administrator_in_db

  return administrator_in_db

def get_administrator(administrator_email: str):
  if administrator_email in database_administrators.keys():
    return database_administrators[administrator_email]
  else:
    return None