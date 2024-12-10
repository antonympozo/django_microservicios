from ninja import NinjaAPI
from typing import List
from .models import Usuario
from .schemas import UserSchema, UserSchemaOut, UserSchemaUpdate
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.post("/usuarios")
def create_user(request, user: UserSchema):
    usuario = Usuario.objects.create(
        nombre=user.nombre,
        apellido_paterno=user.apellido_paterno,
        apellido_materno=user.apellido_materno,
        edad=user.edad,
        nombre_cuenta=user.nombre_cuenta,
        contrasena=user.contrasena
    )
    return {"id": usuario.id}

@api.get("/usuarios", response=List[UserSchemaOut])
def list_users(request):
    return Usuario.objects.all()

@api.get("/usuarios/{user_id}", response=UserSchemaOut)
def get_user(request, user_id: int):
    return get_object_or_404(Usuario, id=user_id)

@api.put("/usuarios/{user_id}")
def update_user(request, user_id: int, user: UserSchemaUpdate):
    usuario = get_object_or_404(Usuario, id=user_id)
    
    for attr, value in user.dict(exclude_unset=True).items():
        setattr(usuario, attr, value)
    
    usuario.save()
    return {"success": True}

@api.delete("/usuarios/{user_id}")
def delete_user(request, user_id: int):
    usuario = get_object_or_404(Usuario, id=user_id)
    usuario.delete()
    return {"success": True}