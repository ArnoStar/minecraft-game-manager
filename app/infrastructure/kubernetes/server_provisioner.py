from kubernetes.client import (
    ApiClient,
    CoreV1Api,
    V1Container,
    V1ContainerPort,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
    V1Service,
    V1ServicePort,
    V1ServiceSpec,
)
from kubernetes.watch.watch import Watch

from app.domain.entities.server import Server
from app.domain.value_object.server_endpoint import ServerEndpoint
from app.domain.value_object.server_types import ServerTypes

import asyncio


class K8sServerProvisioner:
    containers: dict[ServerTypes, str] = {
        ServerTypes.PREMIER: "arnostar/default-server:0.1"
    }

    def __init__(self, client: ApiClient, namespace: str) -> None:
        self.api_client: ApiClient = client
        self.namespace: str = namespace
        self._core: CoreV1Api = CoreV1Api(self.api_client)

        self.watcher: Watch = Watch()

    @staticmethod
    def get_pod_name(server: Server) -> str:
        return f"minecraft-{server.id}"

    async def create_server(self, server: Server) -> None:
        image = self.containers[server.type]
        name = self.get_pod_name(server)

        pod = V1Pod(
            metadata=V1ObjectMeta(
                name=name,
                labels={
                    "minecraft-server": str(server.id),
                },
            ),
            spec=V1PodSpec(
                containers=[
                    V1Container(
                        name="minecraft",
                        image=image,
                        ports=[
                            V1ContainerPort(
                                container_port=25565,
                                protocol="TCP",
                            ),
                        ],
                    ),
                ],
            ),
        )

        service = V1Service(
            metadata=V1ObjectMeta(
                name=name,
            ),
            spec=V1ServiceSpec(
                selector={
                    "minecraft-server": str(server.id),
                },
                ports=[
                    V1ServicePort(
                        port=25565,
                        target_port=25565,
                        protocol="TCP",
                    ),
                ],
            ),
        )

        await asyncio.to_thread(
            self._core.create_namespaced_pod,
            namespace=self.namespace,
            body=pod,
        )

        await asyncio.to_thread(
            self._core.create_namespaced_service,
            namespace=self.namespace,
            body=service,
        )

        server.end_point = ServerEndpoint(
            host=name,
            port=25565,
        )

    async def watch_pods(self):
        queue = asyncio.Queue()

        def blocking_watch():
            for event in self.watcher.stream(
                self._core.list_namespaced_pod,
                namespace=self.namespace,
                label_selector="minecraft-server",
            ):
                asyncio.run_coroutine_threadsafe(
                    queue.put(event),
                    loop,
                )

        loop = asyncio.get_running_loop()
        asyncio.create_task(asyncio.to_thread(blocking_watch))

        while True:
            event = await queue.get()
            yield event
