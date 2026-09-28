from app.core.dtos.role import RoleCreateDTO, RoleResponseDTO
from app.core.entities.role import Role
from app.core.ports.role import RoleRepositoryPort


class CreateRoleUseCase:
    def __init__(self, role_repository: RoleRepositoryPort) -> None:
        self.role_repository = role_repository

    async def execute(self, dto: RoleCreateDTO) -> RoleResponseDTO:
        existing = await self.role_repository.get_by_name(dto.name)
        if existing:
            raise ValueError(f"Role with name '{dto.name}' already exists")

        role = Role(name=dto.name, description=dto.description)
        created_role = await self.role_repository.create(role)

        return RoleResponseDTO(
            id=created_role.id,
            name=created_role.name,
            description=created_role.description,
        )