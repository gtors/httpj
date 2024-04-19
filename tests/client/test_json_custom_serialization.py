from __future__ import annotations

import datetime
from typing import Any
from unittest.mock import Mock

import orjson
import pytest

import httpj


def foo_deserializer(_: Any) -> dict[str, str]:
    return {"foo": "bar"}


@pytest.fixture
def json_serializer() -> Mock:
    mock = Mock()
    mock.side_effect = lambda obj: orjson.dumps(obj, option=orjson.OPT_NAIVE_UTC)
    return mock


@pytest.mark.parametrize(
    "method", ["get", "options", "head", "delete", "post", "put", "patch"]
)
def test_json_deserializer(server, method):
    with httpj.Client(http2=True) as client:
        http_method = getattr(client, method)
        response = http_method(server.url, json_deserialize=foo_deserializer)
        assert response.json() == {"foo": "bar"}

    http_method = getattr(httpj, method)
    response = http_method(server.url, json_deserialize=foo_deserializer)
    assert response.json() == {"foo": "bar"}


@pytest.mark.parametrize("method", ["post", "patch", "put"])
def test_json_serializer(server, method, json_serializer):
    with httpj.Client() as client:
        http_method = getattr(client, method)
        response = http_method(
            server.url,
            json={"dt": datetime.datetime.utcnow()},
            json_serialize=json_serializer,
        )
        assert response.status_code == 200
        assert response.reason_phrase == "OK"
        json_serializer.assert_called_once()

    json_serializer.reset_mock()
    http_method = getattr(httpj, method)
    response = http_method(
        server.url,
        json={"dt": datetime.datetime.utcnow()},
        json_serialize=json_serializer,
    )
    assert response.status_code == 200
    assert response.reason_phrase == "OK"
    json_serializer.assert_called_once()
