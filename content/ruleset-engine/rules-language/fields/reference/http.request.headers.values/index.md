<h1 id="http-request-headers-values">http.request.headers.values</h1>

**Data type:** Array<String>

<p>The values of the headers in the HTTP request.</p>

<p>The values are not pre-processed and retain the original case used in the request.</p>
<p>The order of header values is not guaranteed but will match <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.names/"><code>http.request.headers.names</code></a>.</p>
<p>Duplicate headers are listed multiple times.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p>When the HTTP request contains too many headers, this field may not contain the values of all of the headers sent in the HTTP request. In this situation, the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><code>http.request.headers.truncated</code></a> field will be set to <code>true</code>.</p>
<p><strong>Note</strong>: In HTTP/2, the names of HTTP headers are always in lowercase. Recent versions of the <code>curl</code> tool <a href="https://curl.se/docs/manpage.html#--http2">enable HTTP/2 by default</a> for HTTPS connections.</p>

**Example value:**

```txt
Example 1: ["application/json"]
Example 2: ["This header value is longer than 10 bytes"]
```

**Example usage:**

```txt
# Example 1: Check for specific header value.
any(http.request.headers.values[*] == "application/json")

# Example 2: Match requests according to the specified operator and the length/size entered for the header value.
any(len(http.request.headers.values[*])[*] gt 10)
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor

