from typing import Optional
from app.core.dtos.role import RoleResponseDTO
from app.core.ports.role import RoleRepositoryPort


class GetRoleByIdUseCase:
    def __init__(self, role_repository: RoleRepositoryPort):
        self.role_repository = role_repository

    def execute(self, role_id: int) -> Optional[RoleResponseDTO]:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return None
        return RoleResponseDTO.model_validate(role)