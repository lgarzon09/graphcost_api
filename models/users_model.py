from pydantic import BaseModel

class UsersIn(BaseModel):
  use_email: str
  use_password: str  

class UsersOut(BaseModel):
  use_id: int = 0