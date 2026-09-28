from typing import Optional
from pydantic import BaseModel, ConfigDict


class RoleBaseDTO(BaseModel):
    name: str
    description: Optional[str] = None


class RoleCreateDTO(RoleBaseDTO):
    pass


class RoleResponseDTO(RoleBaseDTO):
    id: int

    model_config = ConfigDict(from_attributes=True)