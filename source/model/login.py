from pydantic import BaseModel

class User(BaseModel):
    full_name: str
    email: str 
    # terms: bool
    # politics: bool
