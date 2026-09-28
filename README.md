# PortScout

A Python port scanner with TCP connect and SYN scanning, built to learn network security fundamentals.

## Features
- TCP connect scanning (v0.1, in progress)

## Installation
```bash
git clone https://github.com/<your-username>/portscout.git
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