import typing

import pytest

import httpj


def test_get(server):
    response = httpj.get(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"
    assert response.text == "Hello, world!"
    assert response.http_version == "HTTP/1.1"


def test_post(server):
    response = httpj.post(server.url, content=b"Hello, world!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_post_byte_iterator(server):
    def data() -> typing.Iterator[bytes]:
        yield b"Hello"
        yield b", "
        yield b"world!"

    response = httpj.post(server.url, content=data())
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_post_byte_stream(server):
    class Data(httpj.SyncByteStream):
        def __iter__(self):
            yield b"Hello"
            yield b", "
            yield b"world!"

    response = httpj.post(server.url, content=Data())
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_options(server):
    response = httpj.options(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_head(server):
    response = httpj.head(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_put(server):
    response = httpj.put(server.url, content=b"Hello, world!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_patch(server):
    response = httpj.patch(server.url, content=b"Hello, world!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_delete(server):
    response = httpj.delete(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_stream(server):
    with httpj.stream("GET", server.url) as response:
        response.read()

    assert response.status_code == 200
    assert response.reason_phrase == "OK"
    assert response.text == "Hello, world!"
    assert response.http_version == "HTTP/1.1"


def test_get_invalid_url():
    with pytest.raises(httpj.UnsupportedProtocol):
        httpj.get("invalid://example.org")


# check that httpcore isn't imported until we do a request
def test_httpcore_lazy_loading(server):
    import sys

    # unload our module if it is already loaded
    if "httpj" in sys.modules:
        del sys.modules["httpj"]
        del sys.modules["httpcore"]
    import httpj

    assert "httpcore" not in sys.modules
    _response = httpj.get(server.url)
    assert "httpcore" in sys.modules
