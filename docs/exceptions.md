# Exceptions

This page lists exceptions that may be raised when using HTTPJ.

For an overview of how to work with HTTPJ exceptions, see [Exceptions (Quickstart)](quickstart.md#exceptions).

## The exception hierarchy

* HTTPError
    * RequestError
        * TransportError
            * TimeoutException
                * ConnectTimeout
                * ReadTimeout
                * WriteTimeout
                * PoolTimeout
            * NetworkError
                * ConnectError
                * ReadError
                * WriteError
                * CloseError
            * ProtocolError
                * LocalProtocolError
                * RemoteProtocolError
            * ProxyError
            * UnsupportedProtocol
        * DecodingError
        * TooManyRedirects
    * HTTPStatusError
* InvalidURL
* CookieConflict
* StreamError
    * StreamConsumed
    * ResponseNotRead
    * RequestNotRead
    * StreamClosed

---

## Exception classes

::: httpj.HTTPError
    :docstring:

::: httpj.RequestError
    :docstring:

::: httpj.TransportError
    :docstring:

::: httpj.TimeoutException
    :docstring:

::: httpj.ConnectTimeout
    :docstring:

::: httpj.ReadTimeout
    :docstring:

::: httpj.WriteTimeout
    :docstring:

::: httpj.PoolTimeout
    :docstring:

::: httpj.NetworkError
    :docstring:

::: httpj.ConnectError
    :docstring:

::: httpj.ReadError
    :docstring:

::: httpj.WriteError
    :docstring:

::: httpj.CloseError
    :docstring:

::: httpj.ProtocolError
    :docstring:

::: httpj.LocalProtocolError
    :docstring:

::: httpj.RemoteProtocolError
    :docstring:

::: httpj.ProxyError
    :docstring:

::: httpj.UnsupportedProtocol
    :docstring:

::: httpj.DecodingError
    :docstring:

::: httpj.TooManyRedirects
    :docstring:

::: httpj.HTTPStatusError
    :docstring:

::: httpj.InvalidURL
    :docstring:

::: httpj.CookieConflict
    :docstring:

::: httpj.StreamError
    :docstring:

::: httpj.StreamConsumed
    :docstring:

::: httpj.StreamClosed
    :docstring:

::: httpj.ResponseNotRead
    :docstring:

::: httpj.RequestNotRead
    :docstring:
