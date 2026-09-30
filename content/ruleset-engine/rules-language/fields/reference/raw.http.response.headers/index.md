<h1 id="raw-http-response-headers">raw.http.response.headers</h1>

**Data type:** Map<Array<String>>

<p>The HTTP response headers without any transformation represented as a Map (or associative array).</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers/"><code>http.response.headers</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>

**Example value:**

```txt
{"server": ["nginx"]}
```

**Example usage:**

```txt
any(raw.http.response.headers["server"][*] == "nginx")
```

<h2 id="categories">Categories</h2>

- Response
- Headers
- Raw fields

**Keywords:** response, raw

