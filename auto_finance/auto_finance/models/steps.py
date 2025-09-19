from pydantic import BaseModel, Field


class Step(BaseModel):
    nome: str
    descricao: str = Field(max_length=240)
    objeto: object
    funcao: str
    etapa: int = 0
