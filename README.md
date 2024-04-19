<p align="center">
  <a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/gtors/httpj/master/docs/img/butterfly.png" alt='HTTPJ'></a>
</p>

<p align="center"><strong>HTTPJ</strong> <em>-A fork of httpx with support for a custom JSON serializer.</em></p>

<p align="center">
<a href="https://github.com/gtors/httpj/actions">
    <img src="https://github.com/encode/httpj/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/httpj/">
    <img src="https://badge.fury.io/py/httpj.svg" alt="Package version">
</a>
</p>

---

Install HTTPJ using pip:

```shell
$ pip install httpj
```

Now, let's get started:

```pycon
>>> import httpj
>>> import orjson
>>> r = httpj.post('https://www.example.org/', json={"foo": "bar"}, json_serialize=orjson.dumps)
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```
