from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    telefone: str
    sigla: str

class UserCreate(BaseModel):
    name: str
    email: str
    telefone: str
    sigla: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    telefone: str | None = None
    sigla: str | None = None