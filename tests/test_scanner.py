import socket

import pytest

from portscout.scanner import parse_ports, scan_port, scan_ports


def test_closed_port_returns_false():
    assert scan_port("127.0.0.1", 1, timeout=0.5) is False


def test_single_ports_are_sorted():
    assert parse_ports("80,22") == [22, 80]


def test_range():
    assert parse_ports("1-3") == [1, 2, 3]


def test_mixed_input_removes_duplicates():
    assert parse_ports("22, 20-23") == [20, 21, 22, 23]


@pytest.mark.parametrize("bad", ["0", "70000", "10-5", "abc", ""])
def test_invalid_input_raises(bad):
    with pytest.raises(ValueError):
        parse_ports(bad)


@pytest.fixture
def open_port():
    """Open a temporary listening port on localhost for the duration of a test."""
    with socket.socket() as server:
        server.bind(("127.0.0.1", 0))  # port 0 = let the OS pick a free port
        server.listen()
        yield server.getsockname()[1]


def test_scan_port_detects_open_port(open_port):
    assert scan_port("127.0.0.1", open_port, timeout=0.5) is True


def test_scan_ports_returns_only_open_ports(open_port):
    assert scan_ports("127.0.0.1", [1, open_port], timeout=0.5) == [open_port]