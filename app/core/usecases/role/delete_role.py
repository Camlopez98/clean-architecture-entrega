from app.core.ports.role import RoleRepositoryPort


class DeleteRoleUseCase:
    def __init__(self, role_repository: RoleRepositoryPort) -> None:
        self.role_repository = role_repository

    async def execute(self, role_id: int) -> bool:
        existing_role = await self.role_repository.get_by_id(role_id)
        if not existing_role:
            return False

        return await self.role_repository.delete(role_id)