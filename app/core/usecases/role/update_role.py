from typing import Optional

from app.core.dtos.role import RoleResponseDTO, RoleUpdateDTO
from app.core.entities.role import Role
from app.core.ports.role import RoleRepositoryPort


class UpdateRoleUseCase:
    def __init__(self, role_repository: RoleRepositoryPort) -> None:
        self.role_repository = role_repository

    async def execute(self, role_id: int, dto: RoleUpdateDTO) -> Optional[RoleResponseDTO]:
        existing_role = await self.role_repository.get_by_id(role_id)
        if not existing_role:
            return None

        # Si cambian el nombre, validar que no choque con otro rol existente
        if dto.name and dto.name != existing_role.name:
            role_with_same_name = await self.role_repository.get_by_name(dto.name)
            if role_with_same_name:
                raise ValueError(f"Role with name '{dto.name}' already exists")
            new_name = dto.name
        else:
            new_name = existing_role.name

        new_desc = dto.description if dto.description is not None else existing_role.description

        role_to_update = Role(
            id=existing_role.id,
            name=new_name,
            description=new_desc,
        )

        updated_role = await self.role_repository.update(role_to_update)
        return RoleResponseDTO(
            id=updated_role.id,
            name=updated_role.name,
            description=updated_role.description,
        )