from pydantic import BaseModel


class Operation(BaseModel):
    pass


class Land(BaseModel):
    coordinates: str
    operation: Operation
