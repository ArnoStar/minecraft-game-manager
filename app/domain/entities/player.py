from dataclasses import dataclass

from app.domain.value_object.elo import Elo

from uuid import UUID


@dataclass
class Player:
    id: UUID
    elo: Elo
