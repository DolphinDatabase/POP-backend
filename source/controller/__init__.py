from .auth_controller import router as auth_router
from .termo_controller import router as termo_router
from .usuario_controller import router as usuario_router
from .gleba_controller import router as gleba_router
from .operacao_controller import router as operacao_router
from .prediction_controller import router as predicrion_router

__all__ = [
    "auth_router",
    "termo_router",
    "usuario_router",
    "gleba_router",
    "operacao_router"
]
