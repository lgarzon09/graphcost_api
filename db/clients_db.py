from typing import Dict
from pydantic import BaseModel

class ClientsInDB(BaseModel):
  cli_id: int
  cli_name: str
  cli_docNumber: str  

database_clients = Dict[str,ClientInDB]

database_clients = {
  "1234567890": ClientsInDB(**{
    "cli_id": 1,
    "cli_name":"Ann A",
    "cli_docNumber":"1234567890"
  }),
  "2468013579": ClientsInDB(**{
    "cli_id": 2,
    "cli_name":"Ben B",
    "cli_docNumber":"2468013579"
  }),
  "1357924680": ClientsInDB(**{
    "cli_id": 3,
    "cli_name":"Dan D",
    "cli_docNumber":"1357924680"
  })
}