import pytest

import httpj


@pytest.mark.anyio
async def test_read_timeout(server):
    timeout = httpj.Timeout(None, read=1e-6)

    async with httpj.AsyncClient(timeout=timeout) as client:
        with pytest.raises(httpj.ReadTimeout):
            await client.get(server.url.copy_with(path="/slow_response"))


@pytest.mark.anyio
async def test_write_timeout(server):
    timeout = httpj.Timeout(None, write=1e-6)

    async with httpj.AsyncClient(timeout=timeout) as client:
        with pytest.raises(httpj.WriteTimeout):
            data = b"*" * 1024 * 1024 * 100
            await client.put(server.url.copy_with(path="/slow_response"), content=data)


@pytest.mark.anyio
@pytest.mark.network
async def test_connect_timeout(server):
    timeout = httpj.Timeout(None, connect=1e-6)

    async with httpj.AsyncClient(timeout=timeout) as client:
        with pytest.raises(httpj.ConnectTimeout):
            # See https://stackoverflow.com/questions/100841/
            await client.get("http://10.255.255.1/")


@pytest.mark.anyio
async def test_pool_timeout(server):
    limits = httpj.Limits(max_connections=1)
    timeout = httpj.Timeout(None, pool=1e-4)

    async with httpj.AsyncClient(limits=limits, timeout=timeout) as client:
        with pytest.raises(httpj.PoolTimeout):
            async with client.stream("GET", server.url):
                await client.get(server.url)


@pytest.mark.anyio
async def test_async_client_new_request_send_timeout(server):
    timeout = httpj.Timeout(1e-6)

    async with httpj.AsyncClient(timeout=timeout) as client:
        with pytest.raises(httpj.TimeoutException):
            await client.send(
                httpj.Request("GET", server.url.copy_with(path="/slow_response"))
            )
