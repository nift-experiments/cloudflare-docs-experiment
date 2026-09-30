<h1 id="http-request-cookies">http.request.cookies</h1>

**Data type:** Map<Array<String>>

<p>The <code>Cookie</code> HTTP header associated with a request represented as a Map (associative array).</p>

<p>Requires a Cloudflare Pro, Business, or Enterprise plan.</p>
<p>The cookie names are URL decoded. If two cookies have the same name after decoding, their value arrays are merged.</p>
<p>The cookie values are not pre-processed and retain the original case used in the request.</p>

**Example value:**

```txt
{ "app": ["test"] }
```

**Example usage:**

```txt
any(http.request.cookies["app"][*] == "test")
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, header, client, visitor

