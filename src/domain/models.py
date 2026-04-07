from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class User:
    email: str
    username: str
    id: UUID = field(default_factory=uuid4)
    is_active: bool = True