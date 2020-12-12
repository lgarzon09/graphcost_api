from typing import Dict
from pydantic import BaseModel

class UsersInDB(BaseModel):
  use_id: int = 0
  use_email: str
  use_password: str  

database_users = Dict[str,UsersInDB]

database_users = {
  "ann@hotel.com": UsersInDB(**{
    "use_id": 1,
    "use_email": "ann@hotel.com",
    "use_password": "1234"
  })
}

generator = {"id": 1}

def save_user(user_in_db: UsersInDB):
  generator["id"] = generator["id"] + 1
  user_in_db.cli_id = generator["id"]

  database_users[client_in_db.use_email] = user_in_db

  return user_in_db

def get_user(use_email: str):
  if use_email in database_users.keys():
    return database_users[use_email]
  else:
    return None
