from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 10  # Updated from 8 to 10

def test_requests_version():
    assert requests_version() == "2.32.3"  # Updated from 2.27.1 to 2.32.3

def test_pytest_version():
    assert pytest_version() == "8.3.3"  # Updated from 7.1.3 to 8.3.3