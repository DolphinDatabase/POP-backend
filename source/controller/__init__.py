from .auth_controller import router as auth_router
from .termo_controller import router as termo_router
from .usuario_controller import router as usuario_router
from .historico_controller import router as historico_router
from .gleba_controller import router as gleba_router
from .operacao_controller import router as operacao_router
from .redis_cache.redis import cache_response as cache_response