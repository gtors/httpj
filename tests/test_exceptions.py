from __future__ import annotations

import typing

import httpcore
import pytest

import httpj

if typing.TYPE_CHECKING:  # pragma: no cover
    from conftest import TestServer


def test_httpcore_all_exceptions_mapped() -> None:
    """
    All exception classes exposed by HTTPCore are properly mapped to an HTTPJ-specific
    exception class.
    """
    expected_mapped_httpcore_exceptions = {
        value.__name__
        for _, value in vars(httpcore).items()
        if isinstance(value, type)
        and issubclass(value, Exception)
        and value is not httpcore.ConnectionNotAvailable
    }

    httpj_exceptions = {
        value.__name__
        for _, value in vars(httpj).items()
        if isinstance(value, type) and issubclass(value, Exception)
    }

    unmapped_exceptions = expected_mapped_httpcore_exceptions - httpj_exceptions

    if unmapped_exceptions:  # pragma: no cover
        pytest.fail(f"Unmapped httpcore exceptions: {unmapped_exceptions}")


def test_httpcore_exception_mapping(server: TestServer) -> None:
    """
    HTTPCore exception mapping works as expected.
    """
    impossible_port = 123456
    with pytest.raises(httpj.ConnectError):
        httpj.get(server.url.copy_with(port=impossible_port))

    with pytest.raises(httpj.ReadTimeout):
        httpj.get(
            server.url.copy_with(path="/slow_response"),
            timeout=httpj.Timeout(5, read=0.01),
        )


def test_request_attribute() -> None:
    # Exception without request attribute
    exc = httpj.ReadTimeout("Read operation timed out")
    with pytest.raises(RuntimeError):
        exc.request  # noqa: B018

    # Exception with request attribute
    request = httpj.Request("GET", "https://www.example.com")
    exc = httpj.ReadTimeout("Read operation timed out", request=request)
    assert exc.request == request
