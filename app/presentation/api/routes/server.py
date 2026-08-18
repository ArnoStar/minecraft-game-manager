from fastapi import APIRouter, Depends

from app.domain.value_object.server_types import ServerTypes
from app.presentation.api.dependencies import Container
from app.presentation.api.schemas.server import CreateServerRequest
from app.application.dtos.server import CreateServerCommand

router = APIRouter(prefix="/server", tags=["Server"])


@router.post("/")
async def add_server(
    server_info_request: CreateServerRequest, container: Container = Depends(Container)
):
    server_info: CreateServerCommand = CreateServerCommand(
        type=ServerTypes(server_info_request.type)
    )

    await container.create_server.execute(server_info)
