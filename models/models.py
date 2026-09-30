from enum import Enum
from pydantic import BaseModel

class Departament(str,Enum):
    TI = "TI"
    RH = "RH"
    FINANCEIRO = "Financeiro"

class Position(str,Enum):
    ESTAGIARIO ="Estagiário"
    ANALISA="Analista"
    SUPERVIDOR = "Supervisor"
    GERENTE="Gerente"
    DIRETOR= "Diretor"

class User(BaseModel):
    id:int 
    name:str
    departament: Departament
    position:Position
    age: int 

class Called(BaseModel):
    id:int
    title :str
    user_id : int
    departament_id : id