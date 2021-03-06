from pydantic import BaseModel

class ClientsIn(BaseModel):
  cli_name: str
  cli_docNumber: str

class ClientsOut(BaseModel):
  cli_id: int
  cli_name: str
  cli_docNumber: str  