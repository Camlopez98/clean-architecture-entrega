from fastapi import APIRouter, HTTPException

from app.core.dtos.role import RoleCreateDTO, RoleResponseDTO
from app.infra.api.dependencies.usecases.role import (
    CreateRole as CreateRoleUsecase,
    GetRoleById as GetRoleByIdUsecase,
)

router = APIRouter()


@router.post(
    "",
    status_code=201,
    summary="Creates new Role",
    response_model=RoleResponseDTO,
)
async def create(dto: RoleCreateDTO, usecase: CreateRoleUsecase) -> RoleResponseDTO:
    try:
        return await usecase.execute(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{role_id}",
    status_code=200,
    summary="Gets Role by ID",
    response_model=RoleResponseDTO,
)
async def get_by_id(role_id: int, usecase: GetRoleByIdUsecase) -> RoleResponseDTO:
    role = await usecase.execute(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role