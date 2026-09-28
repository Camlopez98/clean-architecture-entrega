from abc import ABC, abstractmethod
from typing import Optional

from app.core.entities.role import Role


class RoleRepositoryPort(ABC):
    @abstractmethod
    def create(self, role: Role) -> Role:
        pass

    @abstractmethod
    def get_by_id(self, role_id: int) -> Optional[Role]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Role]:
        pass