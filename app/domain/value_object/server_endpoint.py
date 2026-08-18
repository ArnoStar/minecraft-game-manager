from dataclasses import dataclass

from ipaddress import IPv4Address, IPv6Address


@dataclass(frozen=True)
class ServerEndpoint:
    host: str | IPv4Address | IPv6Address
    port: int

    def __post_init__(self):
        if not self.host:
            raise ValueError("Host cannot be empty")

        if not 1 <= self.port <= 65535:
            raise ValueError("Invalid port")
