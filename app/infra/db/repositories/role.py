from typing import Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.ports.role import RoleRepositoryPort
from app.core.entities.role import Role
from app.infra.db.models.role import Role as RoleModel


class RoleRepository(RoleRepositoryPort):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, role: Role) -> Role:
        db_role = RoleModel(
            name=role.name,
            description=role.description,
        )
        self.session.add(db_role)
        await self.session.commit()
        await self.session.refresh(db_role)
        return Role(
            id=db_role.id,
            name=db_role.name,
            description=db_role.description,
        )

    async def get_by_id(self, role_id: int) -> Optional[Role]:
        statement = select(RoleModel).where(RoleModel.id == role_id)
        result = await self.session.exec(statement)
        db_role = result.first()
        if not db_role:
            return None
        return Role(
            id=db_role.id,
            name=db_role.name,
            description=db_role.description,
        )

    async def get_by_name(self, name: str) -> Optional[Role]:
        statement = select(RoleModel).where(RoleModel.name == name)
        result = await self.session.exec(statement)
        db_role = result.first()
        if not db_role:
            return None
        return Role(
            id=db_role.id,
            name=db_role.name,
            description=db_role.description,
        )