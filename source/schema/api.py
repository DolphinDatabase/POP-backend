from pydantic import BaseModel


class TokenData(BaseModel):
    user: str
    expire: float


class Token(BaseModel):
    access_token: str
    token_type: str
    expire: float
