import pytest

sp = ...
def process_split(config, items) -> None:
    ...

def pytest_report_header(config) -> str:
    ...

def pytest_terminal_summary(terminalreporter) -> None:
    ...

def pytest_addoption(parser) -> None:
    ...

def pytest_collection_modifyitems(config, items) -> None:
    """pytest hook."""
    ...

@pytest.fixture(autouse=True, scope="module")
def file_clear_cache() -> None:
    ...

@pytest.fixture(autouse=True, scope="module")
def check_disabled(request) -> None:
    ...

