from app.core.dtos.role import RoleCreateDTO, RoleResponseDTO
from app.core.entities.role import Role
from app.core.ports.role import RoleRepositoryPort


class CreateRoleUseCase:
    def __init__(self, role_repository: RoleRepositoryPort):
        self.role_repository = role_repository

    def execute(self, dto: RoleCreateDTO) -> RoleResponseDTO:
        existing = self.role_repository.get_by_name(dto.name)
        if existing:
            raise ValueError(f"Role '{dto.name}' already exists.")

        role_entity = Role(
            id=None,
            name=dto.name,
            description=dto.description,
        )
        saved_role = self.role_repository.create(role_entity)
        return RoleResponseDTO.model_validate(saved_role)