from typing import Optional
from sqlmodel import Session, select

from app.core.entities.role import Role as RoleEntity
from app.core.ports.role import RoleRepositoryPort
from app.infra.db.models.role import Role as RoleModel


class RoleRepository(RoleRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def create(self, role: RoleEntity) -> RoleEntity:
        db_role = RoleModel(name=role.name, description=role.description)
        self.session.add(db_role)
        self.session.commit()
        self.session.refresh(db_role)
        return RoleEntity(id=db_role.id, name=db_role.name, description=db_role.description)

    def get_by_id(self, role_id: int) -> Optional[RoleEntity]:
        statement = select(RoleModel).where(RoleModel.id == role_id)
        db_role = self.session.exec(statement).first()
        if not db_role:
            return None
        return RoleEntity(id=db_role.id, name=db_role.name, description=db_role.description)

    def get_by_name(self, name: str) -> Optional[RoleEntity]:
        statement = select(RoleModel).where(RoleModel.name == name)
        db_role = self.session.exec(statement).first()
        if not db_role:
            return None
        return RoleEntity(id=db_role.id, name=db_role.name, description=db_role.description)