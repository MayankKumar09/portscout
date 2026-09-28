import argparse
import socket
import sys
import time

from portscout.scanner import parse_ports, scan_port


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="portscout",
        description="Scan a host for open TCP ports. Only scan systems you are authorized to test.",
    )
    parser.add_argument("target", help="IP address or hostname to scan")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="ports to scan, e.g. 22,80,443 or 1-1024 (default: 1-1024)")
    parser.add_argument("-t", "--timeout", type=float, default=0.5,
                        help="seconds to wait per port (default: 0.5)")
    args = parser.parse_args(argv)

    try:
        ports = parse_ports(args.ports)
    except ValueError as e:
        parser.error(str(e))

    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error(f"could not resolve host '{args.target}'")

    print(f"Scanning {args.target} ({ip}) - {len(ports)} port(s)")
    start = time.perf_counter()
    open_ports = []

    for port in ports:
        if scan_port(ip, port, args.timeout):
            print(f"  {port}/tcp  open")
            open_ports.append(port)

    elapsed = time.perf_counter() - start
    print(f"Done: {len(open_ports)} open port(s) found in {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())