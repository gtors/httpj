import httpj


def hello_world(request: httpj.Request) -> httpj.Response:
    return httpj.Response(200, text="Hello, world")


def test_client_queryparams():
    client = httpj.Client(params={"a": "b"})
    assert isinstance(client.params, httpj.QueryParams)
    assert client.params["a"] == "b"


def test_client_queryparams_string():
    client = httpj.Client(params="a=b")
    assert isinstance(client.params, httpj.QueryParams)
    assert client.params["a"] == "b"

    client = httpj.Client()
    client.params = "a=b"  # type: ignore
    assert isinstance(client.params, httpj.QueryParams)
    assert client.params["a"] == "b"


def test_client_queryparams_echo():
    url = "http://example.org/echo_queryparams"
    client_queryparams = "first=str"
    request_queryparams = {"second": "dict"}
    client = httpj.Client(
        transport=httpj.MockTransport(hello_world), params=client_queryparams
    )
    response = client.get(url, params=request_queryparams)

    assert response.status_code == 200
    assert response.url == "http://example.org/echo_queryparams?first=str&second=dict"
