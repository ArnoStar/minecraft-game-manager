from app.infrastructure.config.settings import settings
from app.infrastructure.kubernetes.server_provisioner import K8sServerProvisioner
from app.infrastructure.kubernetes.kubernetes import create_api_client
from app.application.ports.server_provisioner import ServerProvisioner
from app.application.use_cases.create_server import CreateServer


class Container:
    def __init__(self):
        self.server_provisioner: ServerProvisioner = K8sServerProvisioner(
            create_api_client(),
            settings.kubernetes_namespace,
        )

        self.create_server: CreateServer = CreateServer(
            server_provisioner=self.server_provisioner,
        )
