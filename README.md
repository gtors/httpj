<p align="center">
  <a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/gtors/httpj/master/docs/img/butterfly.png" alt='HTTPJ'></a>
</p>

<p align="center"><strong>HTTPJ</strong> <em>HTTPX fork with custom JSON serializer support.</em></p>

<p align="center">
<a href="https://github.com/gtors/httpj/actions">
    <img src="https://github.com/gtors/httpj/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/httpj/">
    <img src="https://badge.fury.io/py/httpj.svg" alt="Package version">
</a>
</p>

- HTTPJ is nearly identical to HTTPX. The main difference lies in two extra parameters, `json_serialize` and `json_deserialize`, which afford you precise control over the serialization and deserialization of your objects in JSON format.
- HTTPJ will remain synchronized with the mainstream HTTPX until similar functionality emerges.

---

Install HTTPJ using pip:

```shell
pip install httpj
```

Now, let's get started:

```python
import datetime
import pprint

import httpj
import orjson


resp = httpj.post(
    "https://postman-echo.com/post",
    json={"dt": datetime.datetime.utcnow()},
    json_serialize=lambda j: orjson.dumps(j, option=orjson.OPT_NAIVE_UTC),  # optional
    json_deserialize=orjson.loads,  # optional
)
pprint.pprint(resp.json(), indent=4)
```
