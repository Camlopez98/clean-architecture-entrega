from fastapi import APIRouter, HTTPException, status

from app.core.dtos.role import RoleCreateDTO, RoleResponseDTO, RoleUpdateDTO
from app.infra.api.dependencies.usecases.role import (
    CreateRole as CreateRoleUsecase,
    DeleteRole as DeleteRoleUsecase,
    GetRoleById as GetRoleByIdUsecase,
    UpdateRole as UpdateRoleUsecase,
)

router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Creates new Role",
    response_model=RoleResponseDTO,
)
async def create(dto: RoleCreateDTO, usecase: CreateRoleUsecase) -> RoleResponseDTO:
    try:
        return await usecase.execute(dto)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get(
    "/{role_id}",
    status_code=status.HTTP_200_OK,
    summary="Gets Role by ID",
    response_model=RoleResponseDTO,
)
async def get_by_id(role_id: int, usecase: GetRoleByIdUsecase) -> RoleResponseDTO:
    role = await usecase.execute(role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return role


@router.patch(
    "/{role_id}",
    status_code=status.HTTP_200_OK,
    summary="Updates Role information",
    response_model=RoleResponseDTO,
)
async def update(
    role_id: int,
    dto: RoleUpdateDTO,
    usecase: UpdateRoleUsecase,
) -> RoleResponseDTO:
    try:
        updated_role = await usecase.execute(role_id, dto)
        if not updated_role:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        return updated_role
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete(
    "/{role_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletes Role",
)
async def delete(role_id: int, usecase: DeleteRoleUsecase) -> None:
    deleted = await usecase.execute(role_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")