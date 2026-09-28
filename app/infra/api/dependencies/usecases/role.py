from typing import Annotated, AsyncGenerator

from fastapi import Depends

from app.core.ports.role import RoleRepositoryPort
from app.core.usecases.role.create_role import CreateRoleUseCase
from app.core.usecases.role.get_role_by_id import GetRoleByIdUseCase
from app.infra.db import async_session
from app.infra.db.repositories.role import RoleRepository


async def get_role_repo() -> AsyncGenerator[RoleRepositoryPort, None]:
    async with async_session() as session:
        yield RoleRepository(session)


Repo = Annotated[RoleRepositoryPort, Depends(get_role_repo)]


def get_create_role_usecase(repo: Repo) -> CreateRoleUseCase:
    return CreateRoleUseCase(role_repository=repo)


def get_role_by_id_usecase(repo: Repo) -> GetRoleByIdUseCase:
    return GetRoleByIdUseCase(role_repository=repo)


CreateRole = Annotated[CreateRoleUseCase, Depends(get_create_role_usecase)]
GetRoleById = Annotated[GetRoleByIdUseCase, Depends(get_role_by_id_usecase)]