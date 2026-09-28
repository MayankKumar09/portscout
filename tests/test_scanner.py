from portscout.scanner import scan_port

def test_closed_port_returns_false():
    assert scan_port("127.0.0.1", 1, timeout=0.5) is False