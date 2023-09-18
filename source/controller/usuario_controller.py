from fastapi import APIRouter, HTTPException
import service.usuario_service as uService
import schema.usuarioSchema as uSchema

router = APIRouter(
    prefix='/usuario',
    responses={404: {"description": "usuario not found"}}
)

@router.post('/',response_model=uSchema.GetUsuario)
async def create(usuario: uSchema.CreateUsuario):
    return uService.create_usuario(usuario)

@router.get('/{id}', response_model=uSchema.GetUsuario)
async def get(id:int):
    try:
        return uService.get_usuario(id)
    except:
        raise HTTPException(404)

@router.put('/{id}',response_model=uSchema.GetUsuario)
async def update(id:int, usuario: uSchema.UsuarioBase):
    try:
        return uService.update_usuario(id,usuario)
    except:
        raise HTTPException(404)

@router.delete('/{id}')
async def delete(id:int):
    try:
        uService.delete_usuario(id)
    except:
        raise HTTPException(404)