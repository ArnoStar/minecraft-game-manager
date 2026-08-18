from typing import Protocol

from app.domain.entities.server import Server


class ServerProvisioner(Protocol):
    async def create_server(self, server: Server) -> None: ...
