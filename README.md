# PortScout

A Python port scanner with TCP connect and SYN scanning, built to learn network security fundamentals.

## Features
- TCP connect scanning (v0.1, in progress)

## Installation
```bash
git clone https://github.com/MayankKumar09/portscout.git
cd portscout
python -m venv venv
pip install -e .
```

## Usage
```bash
portscout 127.0.0.1 -p 1-1024
portscout scanme.nmap.org -p 22,80,443 -t 1.0
```

Example output:
Scanning 127.0.0.1 (127.0.0.1) - 1024 port(s)
  135/tcp  open
  445/tcp  open
Done: 2 open port(s) found in 520.60s

## Benchmarks
Full scan of ports 1-1024 on localhost (Windows, timeout 0.5s):

| Workers | Time     | Speedup |
|---------|----------|---------|
| 1       | 520.95 s | 1x      |
| 10      | 52.52 s  | 9.9x    |
| 50      | 10.71 s  | 48.6x   |
| 100     | 5.61 s   | 92.9x   |
| 200     | 3.08 s   | 169.1x  |

All runs found the same open ports, so concurrency did not reduce accuracy.

On Windows, closed ports consumed nearly the full timeout, so scan time follows
time ≈ (ports ÷ workers) × timeout. Scanning is I/O-bound, which is why threads
scale almost linearly despite Python's GIL. On remote targets, higher worker
counts trade accuracy and stealth for speed.
## Roadmap
- [x] v0.1 TCP connect scan + CLI
- [ ] v0.2 Multithreading + benchmarks
- [ ] v0.3 Banner grabbing / service detection
- [ ] v0.4 SYN scan with Scapy
- [ ] v0.5 JSON/CSV output, tests, CI
- [ ] v0.6 Accuracy comparison against Nmap

## Legal & Ethical Use
Only scan systems you own or have explicit written permission to test.
Unauthorized scanning may be illegal in your jurisdiction.

## License
MIT
