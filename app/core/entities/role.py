from dataclasses import dataclass
from typing import Optional


@dataclass
class Role:
    id: Optional[int]
    name: str
    description: Optional[str] = None