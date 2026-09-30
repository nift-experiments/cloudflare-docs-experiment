<h1 id="raw-http-response-headers-names">raw.http.response.headers.names</h1>

**Data type:** Array<String>

<p>The names of the headers in the HTTP response without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.names/"><code>http.response.headers.names</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>

**Example value:**

```txt
["content-type"]
```

**Example usage:**

```txt
any(raw.http.response.headers.names[*] == "content-type")
```

<h2 id="categories">Categories</h2>

- Response
- Headers
- Raw fields

**Keywords:** response, raw

