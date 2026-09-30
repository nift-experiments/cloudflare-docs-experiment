<h1 id="raw-http-response-headers-values">raw.http.response.headers.values</h1>

**Data type:** Array<String>

<p>The values of the headers in the HTTP response without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.values/"><code>http.response.headers.values</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>

**Example value:**

```txt
Example 1: ["application/json"]
Example 2: ["This header value is longer than 10 bytes"]
```

**Example usage:**

```txt
# Example 1: Check for specific header value.
any(raw.http.response.headers.values[*] == "application/json")

# Example 2: Match requests according to the specified operator and the length/size entered for the header value.
any(len(raw.http.response.headers.values[*])[*] gt 10)
```

<h2 id="categories">Categories</h2>

- Response
- Headers
- Raw fields

**Keywords:** response, raw

