<h1 id="http-request-headers">http.request.headers</h1>

**Data type:** Map<Array<String>>

<p>The HTTP request headers represented as a Map (or associative array).</p>

<p>The keys of the associative array are the names of HTTP request headers converted to lowercase.</p>
<p>When there are repeating headers, the array includes them in the order they appear in the request.</p>
<p>The request header values are not pre-processed and retain the original case used in the request.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p>When the HTTP request contains too many headers, this field may not contain all of the headers sent in the HTTP request. In this situation, the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><code>http.request.headers.truncated</code></a> field will be set to <code>true</code>.</p>

**Example value:**

```txt
{"content-type": ["application/json"]}
```

**Example usage:**

```txt
any(http.request.headers["content-type"][*] == "application/json")
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor

