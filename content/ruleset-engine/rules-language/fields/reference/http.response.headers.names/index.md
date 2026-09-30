<h1 id="http-response-headers-names">http.response.headers.names</h1>

**Data type:** Array<String>

<p>The names of the headers in the HTTP response.</p>

<p>The names are not pre-processed and retain the original case used in the response.</p>
<p>The order of header names is not guaranteed but will match <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.values/"><code>http.response.headers.values</code></a>.</p>
<p>Duplicate headers are listed multiple times.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

**Example value:**

```txt
["content-type"]
```

**Example usage:**

```txt
any(http.response.headers.names[*] == "content-type")
```

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

