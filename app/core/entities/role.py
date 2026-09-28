from dataclasses import dataclass


@dataclass
class Role:
    name: str
    description: str | None = None
    id: int | None = None