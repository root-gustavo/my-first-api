from pydantic import BaseModel, Field


class User(BaseModel):
    """
    Modelo de usuário retornado pela API.

    Inclui ID e todos os dados do usuário armazenados no banco.
    """

    id: int = Field(..., description="ID único do usuário")
    name: str = Field(..., description="Nome completo do usuário")
    email: str = Field(..., description="E-mail cadastrado")
    telefone: str = Field(..., description="Telefone do usuário")
    sigla: str = Field(..., description="Sigla ou abreviação associada ao usuário")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Gustavo Santos",
                "email": "gustavo@example.com",
                "telefone": "11999999999",
                "sigla": "PR"
            }
        }


class UserCreate(BaseModel):
    """
    Modelo enviado para criar um novo usuário.

    Não contém ID, pois o ID é gerado automaticamente pelo banco.
    """

    name: str = Field(..., description="Nome completo do usuário")
    email: str = Field(..., description="E-mail válido")
    telefone: str = Field(..., description="Telefone no formato string")
    sigla: str = Field(..., description="Sigla ou abreviação")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Ana Souza",
                "email": "ana@example.com",
                "telefone": "11988887777",
                "sigla": "SC"
            }
        }


class UserUpdate(BaseModel):
    """
    Modelo enviado para atualizar parcialmente um usuário.

    Todos os campos são opcionais, ideal para requisições PATCH.
    """

    name: str | None = Field(None, description="Nome atualizado do usuário")
    email: str | None = Field(None, description="Novo e-mail")
    telefone: str | None = Field(None, description="Telefone atualizado")
    sigla: str | None = Field(None, description="Nova sigla")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "novo_email@example.com",
                "telefone": "11944445555"
            }
        }
