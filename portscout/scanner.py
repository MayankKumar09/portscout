import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Return True if a TCP connection to host:port succeeds."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0