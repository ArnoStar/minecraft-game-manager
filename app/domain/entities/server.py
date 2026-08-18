from dataclasses import dataclass, field

from app.domain.value_object.server_types import ServerTypes
from app.domain.value_object.server_endpoint import ServerEndpoint

from uuid import UUID, uuid4


@dataclass
class Server:
    type: ServerTypes
    end_point: ServerEndpoint | None

    id: UUID = field(default_factory=uuid4)
