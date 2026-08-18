from pydantic import BaseModel


class CreateServerRequest(BaseModel):
    type: str
