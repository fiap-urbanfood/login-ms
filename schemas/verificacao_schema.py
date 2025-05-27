from pydantic import BaseModel, EmailStr


class VerificacaoExternaSchema(BaseModel):
    user: str
    cpf: str
    email: EmailStr 