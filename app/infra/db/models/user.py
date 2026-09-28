from typing import TYPE_CHECKING, Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infra.db.models.role import Role


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(primary_key=True)
    name: str
    email: str = Field(unique=True)
    password_hash: str

    # Clave foránea única para forzar relación 1 a 1
    role_id: Optional[int] = Field(default=None, foreign_key="roles.id", unique=True)
    role: Optional["Role"] = Relationship(back_populates="user")