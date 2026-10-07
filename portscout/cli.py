import argparse
import socket
import sys
import time

from portscout.scanner import parse_ports, scan_ports


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
    parser.add_argument("-w", "--workers", type=int, default=100,
                        help="number of ports to scan at once (default: 100)")
    args = parser.parse_args(argv)

    try:
        ports = parse_ports(args.ports)
    except ValueError as e:
        parser.error(str(e))

    if not 1 <= args.workers <= 1000:
        parser.error("workers must be between 1 and 1000")

    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error(f"could not resolve host '{args.target}'")

    print(f"Scanning {args.target} ({ip}) - {len(ports)} port(s), {args.workers} workers")
    start = time.perf_counter()

    open_ports = scan_ports(ip, ports, args.timeout, args.workers)
    for port in open_ports:
        print(f"  {port}/tcp  open")

    elapsed = time.perf_counter() - start
    print(f"Done: {len(open_ports)} open port(s) found in {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())