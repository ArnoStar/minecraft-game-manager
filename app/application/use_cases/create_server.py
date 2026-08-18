from app.domain.entities.server import Server
from app.application.ports.server_provisioner import ServerProvisioner
from app.application.dtos.server import CreateServerCommand


class CreateServer:
    def __init__(self, server_provisioner: ServerProvisioner) -> None:
        self.server_provisioner = server_provisioner

    async def execute(self, server_info: CreateServerCommand) -> None:
        server: Server = Server(
            type=server_info.type,
            end_point=None,
        )

        await self.server_provisioner.create_server(server)
