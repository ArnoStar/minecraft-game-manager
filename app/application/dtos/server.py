from dataclasses import dataclass

from app.domain.value_object.server_types import ServerTypes


@dataclass(frozen=True)
class CreateServerCommand:
    type: ServerTypes
