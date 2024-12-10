from ninja import Schema
from typing import Optional

class UserSchema(Schema):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str
    contrasena: str

class UserSchemaOut(Schema):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str

class UserSchemaUpdate(Schema):
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    edad: Optional[int] = None
    nombre_cuenta: Optional[str] = None
    contrasena: Optional[str] = None